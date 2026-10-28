"""
FINNOAQ OMEGA — Free-Research Acquisition, DOI Verification & Vault Sync Engine
===============================================================================
Project Ref: FNQ-PR-2026-001
Lead Chemical and Process Engineer: Sourish Senapati (FinnoaQ Agro-Industrial Technologies Ltd.)

Implements Part C2 & Part C3 of the FinnoaQ OMEGA Mandate:
- Queries supported public scientific APIs:
  1. Crossref REST API (https://api.crossref.org/works)
  2. OpenAlex API (https://api.openalex.org/works)
  3. Europe PMC REST API (https://www.ebi.ac.uk/europepmc/webservices/rest/search)
  4. Unpaywall DOI Lookup API (https://api.unpaywall.org/v2/{doi} — strictly DOI-based
     lookup; the Unpaywall search endpoint retired on 18 September 2026 is prohibited).
- Caches source metadata and raw responses locally in `evidence_vault/raw_queries/`.
- Deduplicates by normalized DOI and classifies species/material relevance:
  (`DIRECT_CAJANUS_CAJAN_SPLIT`, `INDIRECT_CAJANUS_CAJAN_WHOLE`, `INDIRECT_OTHER_PULSE`,
   `GENERAL_ENGINEERING_OR_STANDARD`, `MISMATCHED_UNRELATED`).
- Operates offline-first from local cache whenever network is unavailable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

_RESOLVED_PARENT = Path(__file__).resolve().parent.parent.parent
ROOT = _RESOLVED_PARENT.parent if _RESOLVED_PARENT.name == "toor_dal_optimization" else _RESOLVED_PARENT
VAULT_DIR = ROOT / "evidence_vault"
RAW_CACHE_DIR = VAULT_DIR / "raw_queries"

USER_AGENT = "FinnoaQ-OMEGA-ResearchVault/2.0 (Project: FNQ-PR-2026-001; mailto:sourish.senapati@finnoaq.com)"
UNPAYWALL_EMAIL = os.environ.get("FINNOAQ_UNPAYWALL_EMAIL", "sourish.senapati@finnoaq.com")


def normalize_doi(doi_or_url: str) -> str:
    """Normalize a DOI or doi.org URL to lowercase bare DOI."""
    s = doi_or_url.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if s.lower().startswith(prefix):
            s = s[len(prefix):]
    return s.strip().lower()


def classify_material_relevance(title: str, abstract: str = "") -> str:
    """Classify whether a paper addresses split pigeon pea, whole pigeon pea, another pulse, or general methods."""
    blob = f"{title} {abstract}".lower()
    if any(k in blob for k in ("impingement", "beef", "pork", "poultry", "plum")):
        if not any(p in blob for p in ("cajanus", "pigeon pea", "pigeonpea", "red gram", "toor", "arhar")):
            return "MISMATCHED_UNRELATED"
    has_pigeon_pea = any(p in blob for p in ("cajanus", "pigeon pea", "pigeonpea", "red gram", "toor", "arhar"))
    has_split = any(s in blob for s in ("split", "dhal", "dal", "dehulled", "decorticated", "cotyledon"))
    if has_pigeon_pea and has_split:
        return "DIRECT_CAJANUS_CAJAN_SPLIT"
    if has_pigeon_pea:
        return "INDIRECT_CAJANUS_CAJAN_WHOLE"
    if any(p in blob for p in ("legume", "pulse", "phaseolus", "bean", "chickpea", "lentil", "vigna", "pea")):
        return "INDIRECT_OTHER_PULSE"
    return "GENERAL_ENGINEERING_OR_STANDARD"


def _http_get_json(url: str, timeout: float = 8.0, retries: int = 2) -> Optional[Dict[str, Any]]:
    """Perform a polite HTTP GET request with User-Agent, optional OpenAlex key, and retry backoff."""
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    openalex_key = os.environ.get("OPENALEX_API_KEY")
    if openalex_key and "api.openalex.org" in url:
        headers["Authorization"] = f"Bearer {openalex_key}"

    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError):
            if attempt < retries:
                time.sleep(0.6 * (attempt + 1))
    return None


def verify_doi_across_apis(doi: str, use_network: bool = True) -> Dict[str, Any]:
    """
    Verify a single DOI via Crossref, OpenAlex, and Unpaywall (DOI-endpoint only),
    caching the result in `evidence_vault/raw_queries/`.
    """
    RAW_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    clean_doi = normalize_doi(doi)
    safe_slug = clean_doi.replace("/", "__").replace(".", "_")
    cache_file = RAW_CACHE_DIR / f"doi_verify_{safe_slug}.json"

    if cache_file.exists() and not use_network:
        return json.loads(cache_file.read_text(encoding="utf-8"))

    result: Dict[str, Any] = {
        "doi": clean_doi,
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
        "crossref": None,
        "openalex": None,
        "unpaywall_oa": None,
        "resolved_title": None,
        "resolved_year": None,
        "resolved_journal": None,
        "resolved_authors": [],
        "is_open_access": False,
        "oa_url": None,
        "license": None,
        "species_applicability": "UNKNOWN",
        "verification_status": "UNVERIFIED_OFFLINE",
    }

    if use_network:
        # 1. Crossref REST API
        cr_url = f"https://api.crossref.org/works/{urllib.parse.quote(clean_doi, safe='')}"
        cr_data = _http_get_json(cr_url)
        if cr_data and "message" in cr_data:
            msg = cr_data["message"]
            title = (msg.get("title") or [""])[0]
            year = (msg.get("issued", {}).get("date-parts") or [[None]])[0][0]
            journal = (msg.get("container-title") or [""])[0]
            authors = [
                f"{a.get('family', '')}, {a.get('given', '')}".strip(", ")
                for a in msg.get("author", [])
            ]
            result["crossref"] = {"status": "FOUND", "title": title, "year": year, "journal": journal}
            result["resolved_title"] = title
            result["resolved_year"] = year
            result["resolved_journal"] = journal
            result["resolved_authors"] = authors
            result["verification_status"] = "VERIFIED_ONLINE"

        # 2. OpenAlex API
        oa_url = f"https://api.openalex.org/works/https://doi.org/{clean_doi}"
        oa_data = _http_get_json(oa_url)
        if oa_data and oa_data.get("id"):
            result["openalex"] = {
                "id": oa_data.get("id"),
                "title": oa_data.get("title"),
                "publication_year": oa_data.get("publication_year"),
                "cited_by_count": oa_data.get("cited_by_count"),
                "is_oa": oa_data.get("open_access", {}).get("is_oa", False),
                "oa_url": oa_data.get("open_access", {}).get("oa_url"),
            }
            if not result["resolved_title"]:
                result["resolved_title"] = oa_data.get("title")
                result["resolved_year"] = oa_data.get("publication_year")
                result["verification_status"] = "VERIFIED_ONLINE"
            if oa_data.get("open_access", {}).get("is_oa"):
                result["is_open_access"] = True
                result["oa_url"] = oa_data.get("open_access", {}).get("oa_url")

        # 3. Unpaywall DOI-Lookup API (Never use the retired /v2/search endpoint)
        upw_url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(clean_doi, safe='')}?email={urllib.parse.quote(UNPAYWALL_EMAIL)}"
        upw_data = _http_get_json(upw_url)
        if upw_data and upw_data.get("doi"):
            best_oa = upw_data.get("best_oa_location") or {}
            result["unpaywall_oa"] = {
                "is_oa": upw_data.get("is_oa", False),
                "oa_status": upw_data.get("oa_status"),
                "url_for_pdf": best_oa.get("url_for_pdf"),
                "license": best_oa.get("license"),
            }
            if upw_data.get("is_oa"):
                result["is_open_access"] = True
                result["oa_url"] = best_oa.get("url_for_pdf") or best_oa.get("url") or result["oa_url"]
                result["license"] = best_oa.get("license")

    if result["resolved_title"]:
        result["species_applicability"] = classify_material_relevance(result["resolved_title"])
        cache_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    elif cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))

    return result


def search_multi_api_literature(query: str, max_results: int = 5, use_network: bool = True) -> Dict[str, Any]:
    """
    Search OpenAlex, Europe PMC, and Crossref for a scientific query, deduplicate by DOI,
    classify species relevance, and cache locally.
    """
    RAW_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    slug = "".join(c if c.isalnum() else "_" for c in query.lower())[:50]
    cache_path = RAW_CACHE_DIR / f"search_{slug}.json"

    if cache_path.exists() and not use_network:
        return json.loads(cache_path.read_text(encoding="utf-8"))

    dedup_by_doi: Dict[str, Dict[str, Any]] = {}

    if use_network:
        # 1. OpenAlex Search
        oa_q = urllib.parse.quote(query)
        oa_res = _http_get_json(f"https://api.openalex.org/works?search={oa_q}&per-page={max_results}")
        if oa_res and "results" in oa_res:
            for item in oa_res["results"]:
                doi_raw = item.get("doi") or item.get("id", "")
                doi = normalize_doi(doi_raw)
                title = item.get("title") or ""
                if doi and title:
                    dedup_by_doi[doi] = {
                        "doi": doi,
                        "title": title,
                        "year": item.get("publication_year"),
                        "source_api": "OpenAlex",
                        "is_open_access": item.get("open_access", {}).get("is_oa", False),
                        "oa_url": item.get("open_access", {}).get("oa_url"),
                        "cited_by_count": item.get("cited_by_count", 0),
                        "species_applicability": classify_material_relevance(title),
                    }

        # 2. Europe PMC REST API Search
        epmc_q = urllib.parse.quote(query)
        epmc_res = _http_get_json(
            f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={epmc_q}&format=json&pageSize={max_results}"
        )
        if epmc_res and "resultList" in epmc_res:
            for item in epmc_res["resultList"].get("result", []):
                doi = normalize_doi(item.get("doi", ""))
                title = item.get("title", "")
                if doi and title and doi not in dedup_by_doi:
                    dedup_by_doi[doi] = {
                        "doi": doi,
                        "title": title,
                        "year": int(item["pubYear"]) if str(item.get("pubYear", "")).isdigit() else None,
                        "source_api": "EuropePMC",
                        "is_open_access": item.get("isOpenAccess") == "Y",
                        "oa_url": f"https://europepmc.org/article/{item.get('source','MED')}/{item.get('id','')}",
                        "cited_by_count": item.get("citedByCount", 0),
                        "species_applicability": classify_material_relevance(title),
                    }

        # 3. Crossref REST API Search
        cr_q = urllib.parse.quote(query)
        cr_res = _http_get_json(f"https://api.crossref.org/works?query={cr_q}&rows={max_results}")
        if cr_res and "message" in cr_res:
            for item in cr_res["message"].get("items", []):
                doi = normalize_doi(item.get("DOI", ""))
                title = (item.get("title") or [""])[0]
                year = (item.get("issued", {}).get("date-parts") or [[None]])[0][0]
                if doi and title and doi not in dedup_by_doi:
                    dedup_by_doi[doi] = {
                        "doi": doi,
                        "title": title,
                        "year": year,
                        "source_api": "Crossref",
                        "is_open_access": False,
                        "oa_url": None,
                        "cited_by_count": item.get("is-referenced-by-count", 0),
                        "species_applicability": classify_material_relevance(title),
                    }

    payload = {
        "query": query,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_deduplicated": len(dedup_by_doi),
        "results": list(dedup_by_doi.values()),
    }
    raw_bytes = json.dumps(payload, sort_keys=True).encode("utf-8")
    payload["content_sha256"] = hashlib.sha256(raw_bytes).hexdigest()
    if dedup_by_doi:
        cache_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    elif cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    return payload


def run_citation_audit(use_network: bool = True) -> Dict[str, Any]:
    """
    Execute Gate 1 / C2 citation audit across key DOIs, explicitly checking the
    Nisha et al. (2006) texture vs riboflavin vs air-impingement DOI triplet.
    """
    target_dois = [
        "10.1016/j.jfoodeng.2005.02.021",  # Misattributed air-impingement study
        "10.1016/j.jfoodeng.2005.05.054",  # Nisha et al. (2006) Texture kinetics in potato, green gram and red gram
        "10.1016/j.jfoodeng.2005.05.056",  # Nisha et al. (2006) Riboflavin degradation kinetics in red gram splits
        "10.1016/j.lwt.2021.111191",       # Vasquez, Siche & Miano (2021) Ultrasound + NaHCO3 whole pigeon pea
        "10.1016/j.meafoo.2024.100176",    # Ohanenye et al. (2024) Pigeon pea protein changes under NaHCO3
        "10.1016/j.jfoodeng.2006.10.019",  # Chakraborty, Kumbhar & Sarkar (2007) Instant pigeonpea dhal RSM
        "10.1016/j.foodchem.2023.135743",  # Perera et al. (2023) HTC review
        "10.1021/acsfoodscitech.5c00916",  # Panda et al. (2026) HTC pulses review
        "10.3389/fsufs.2025.1613117",      # Machinjili et al. (2025) Dehulling East African pigeon pea genotypes
        "10.1111/j.1365-2621.1988.tb07849.x",  # Shepherd & Bhardwaj (1988) Thin-layer drying of pigeon pea
        "10.1016/0260-8774(95)00005-4",    # Fito et al. (1996) Vacuum impregnation HDM
        "10.1111/1541-4337.12244",         # Roland et al. (2017) Pulse off-flavors and LOX
    ]
    records = {}
    for d in target_dois:
        records[d] = verify_doi_across_apis(d, use_network=use_network)

    audit_summary = {
        "project_ref": "FNQ-PR-2026-001",
        "audited_at_utc": datetime.now(timezone.utc).isoformat(),
        "nisha_2006_doi_disambiguation": {
            "10.1016/j.jfoodeng.2005.02.021": {
                "resolved_title": records["10.1016/j.jfoodeng.2005.02.021"].get("resolved_title"),
                "status": "REJECTED_CITATION_MISMATCH (FAIL-0026: Air impingement study, NOT red gram texture)",
            },
            "10.1016/j.jfoodeng.2005.05.054": {
                "resolved_title": records["10.1016/j.jfoodeng.2005.05.054"].get("resolved_title"),
                "status": "PRIMARY_TEXTURE_KINETICS_SOURCE (Nisha, Singhal & Pandit, 2006, J. Food Eng. 74:108-115)",
            },
            "10.1016/j.jfoodeng.2005.05.056": {
                "resolved_title": records["10.1016/j.jfoodeng.2005.05.056"].get("resolved_title"),
                "status": "COMPLEMENTARY_NUTRIENT_SOURCE (Nisha et al., 2006, J. Food Eng. 76:524-530, Riboflavin degradation in red gram splits)",
            },
        },
        "verified_dois": records,
    }
    RAW_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    out_file = RAW_CACHE_DIR / "doi_verification_audit.json"
    out_file.write_text(json.dumps(audit_summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return audit_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="FinnoaQ OMEGA Free-Research Acquisition & DOI Verification CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_verify = sub.add_parser("verify-dois", help="Verify catalog DOIs against Crossref, OpenAlex, and Unpaywall")
    p_verify.add_argument("--offline", action="store_true", help="Use cached responses only")

    p_search = sub.add_parser("search", help="Search OpenAlex, Europe PMC, and Crossref")
    p_search.add_argument("query", type=str, help="Search query string")
    p_search.add_argument("--max-results", type=int, default=5)
    p_search.add_argument("--offline", action="store_true")

    args = parser.parse_args()
    if args.cmd == "search":
        res = search_multi_api_literature(args.query, max_results=args.max_results, use_network=not args.offline)
        print(json.dumps(res, indent=2))
    else:
        res = run_citation_audit(use_network=not getattr(args, "offline", False))
        print(json.dumps(res["nisha_2006_doi_disambiguation"], indent=2))


if __name__ == "__main__":
    main()

