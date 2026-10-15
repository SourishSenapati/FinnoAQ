# PLANT LAYOUT AND HYGIENIC ZONING (15 MT/DAY PLANT)
**Document ID:** ENG-REP-15T-008  
**Revision:** 1.0 | **Date:** 15 October 2026  
**Status:** `PRELIMINARY_CALCULATED` — **WARNING: PRELIMINARY—NOT FOR CONSTRUCTION**  
**Engineering Discipline:** Civil, Plant Architecture & Food Hygiene  

---

## 1. Plant Plot Plan & Spatial Architecture

The 15 MT/day facility is laid out in a linear, unidirectional material flow building measuring **45.0 m length $\times$ 20.0 m width** ($900.0\text{ m}^2$ covered factory area) on a standard industrial plot ($60\text{ m} \times 35\text{ m} = 2,100\text{ m}^2$).

```mermaid
graph LR
    subgraph Plot Plan Layout (45m x 20m)
        Z1[Zone 1: Raw Intake 10m x 20m] -->|Air Barrier| Z2[Zone 2: Wet Soaking 10m x 20m]
        Z2 -->|Wall Penetration| Z3[Zone 3: Drying 12m x 20m]
        Z3 -->|Hygiene Airlock| Z4[Zone 4: High-Care Pack 13m x 20m]
    end
    
    subgraph External Utilities
        Z5[Zone 5: Boiler, ETP, CIP 15m x 10m]
    end
```

---

## 2. Five-Tier Hygienic Zoning Architecture

In strict accordance with FSSAI Schedule 4 (General Sanitary and Hygienic Requirements) and Codex Alimentarius guidelines, the plant is partitioned into five physical hygiene zones separated by full-height insulated sandwich PUF panel walls:

| Hygiene Zone | Area Dimensions | Processing Operations | Floor / Wall Finish | Air Handling / Pressure | Hygiene Barrier Requirements |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Zone 1: Raw Grain Intake** | $10\text{m} \times 20\text{m}$ ($200\text{ m}^2$) | Bag unloading, `HOP-101`, `EL-101`, `SCN-101` destoner | Heavy-duty concrete with hardener, epoxy painted | Ambient, local dust aspiration hoods (BH-101) | Roll-up motorized shutter, insect air curtain |
| **Zone 2: Wet Soaking & Dosing** | $10\text{m} \times 20\text{m}$ ($200\text{ m}^2$) | `TK-100`, `P-100`, `TK-101A/B`, `VS-101` dewatering | Chemical-resistant polyurea coating, anti-slip | Neutral air, mechanical exhaust over tanks | Footbath with sanitizing foam, rubber boots |
| **Zone 3: Thermal Drying & Air Handling**| $12\text{m} \times 20\text{m}$ ($240\text{ m}^2$) | `DR-101`, `CLR-101`, `FN-101`, `CYC-101` cyclone | Polyurethane screed ($4\text{ mm}$), thermal resistant | Filtered makeup air (MERV 8), negative exhaust | Airlock swing doors, personnel hand wash station |
| **Zone 4: High-Care Packaging & Warehouse**| $13\text{m} \times 20\text{m}$ ($260\text{ m}^2$) | `HOP-102`, `MD-101`, `PK-101`, `CW-101`, palletizing | High-gloss self-leveling epoxy ($3\text{ mm}$), coved corners | **Positive pressure (+15 Pa), MERV 14 / EU9 filtered air** | **Full gowning room, shoe change, automatic hand wash/dry** |
| **Zone 5: Utilities & Environmental**| $15\text{m} \times 10\text{m}$ ($150\text{ m}^2$) | Steam boiler, `ETP-101`, `CIP-101`, air compressor | External RCC slab with bund walls and acid tiles | Outdoor / ventilated utility shed | Segregated external access gate, hazardous chemical bund |

---

## 3. Floor Drainage and Sloping Engineering

Wet processing introduces significant microbial and slip hazards if liquid pools on floors. The drainage philosophy enforces:
- **Floor Slope:** Minimum $1:50$ ($2.0\%$) slope on all Zone 2 floors leading directly to central drainage trenches.
- **Drainage Channels:** Continuous SS304 Euro-trough hygienic box drains ($200\text{ mm}$ wide, radius bottom) fitted with heavy-duty anti-slip heel-proof slot gratings.
- **Odor & Pest Traps:** Deep removable SS304 foul-air U-traps and silt baskets installed at every drain discharge junction to prevent sewer flies, cockroaches, and drain biofilm back-contamination.
- **Zero Cross-Drainage:** Complete hydraulic isolation between Zone 2 (wet chemical effluent) and Zone 4 (dry packaging). No open drain crosses a hygiene partition wall.

---

## 4. Personnel & Logistics Flow Architecture

- **Raw Material Intake:** 40-foot container trucks dock at the western bay (Zone 1). Dry bags are palletized and unloaded directly into hopper `HOP-101`.
- **Chemical Delivery:** Food-grade sodium bicarbonate bags arrive via a dedicated exterior door to the Chemical Storage Room in Zone 2, completely bypassing food processing corridors.
- **Personnel Entry:** Plant operators enter through the central hygiene lock: street shoes removed $\rightarrow$ factory footwear donned $\rightarrow$ hand wash with warm water and bactericidal soap $\rightarrow$ alcohol mist hand sanitizer $\rightarrow$ hair net / beard snood $\rightarrow$ entrance into packaging hall (Zone 4) under positive air pressure.
- **Finished Goods Dispatch:** Sealed retail pouches packed in corrugated shipper cartons exit through high-speed automatic dock doors on the eastern facade (Zone 4) directly into dispatch trucks.
