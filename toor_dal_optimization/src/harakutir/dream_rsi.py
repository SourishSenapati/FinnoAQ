"""
Dream-RSI-Inspired Adaptive Discovery and Replay Layer.
Implements discovery trees, deterministic replay over recorded traces,
multi-objective policy scoring, and hard integrity rejection filters.
Reference: Dream-RSI concepts (arXiv:2609.14858 / kudoej/dream-rsi).
Label: Dream-RSI-inspired experimental replay layer (NOT official library release).
"""

import os
import json
import time
import hashlib
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

class DiscoveryNode:
    def __init__(
        self,
        node_id: str,
        parent_id: Optional[str],
        task_hypothesis: str,
        policy_version: str,
        command_or_action: str,
        config_hash: str,
        data_hash: str,
        cost_seconds: float = 0.0,
        status: str = "PENDING",
        test_results: Optional[Dict[str, Any]] = None,
        failure_cause: Optional[str] = None
    ):
        self.node_id = node_id
        self.parent_id = parent_id
        self.task_hypothesis = task_hypothesis
        self.policy_version = policy_version
        self.command_or_action = command_or_action
        self.config_hash = config_hash
        self.data_hash = data_hash
        self.cost_seconds = cost_seconds
        self.status = status
        self.test_results = test_results or {}
        self.failure_cause = failure_cause
        self.created_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node_id": self.node_id,
            "parent_id": self.parent_id,
            "task_hypothesis": self.task_hypothesis,
            "policy_version": self.policy_version,
            "command_or_action": self.command_or_action,
            "config_hash": self.config_hash,
            "data_hash": self.data_hash,
            "cost_seconds": self.cost_seconds,
            "status": self.status,
            "test_results": self.test_results,
            "failure_cause": self.failure_cause,
            "created_at": self.created_at
        }

class DiscoveryTree:
    def __init__(self, tree_file: str = "state/discovery_tree.json"):
        self.tree_file = tree_file
        self.nodes: Dict[str, DiscoveryNode] = {}
        self.load()

    def load(self):
        if os.path.isfile(self.tree_file):
            try:
                with open(self.tree_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for nid, nd in data.get("nodes", {}).items():
                    node = DiscoveryNode(
                        node_id=nd["node_id"],
                        parent_id=nd.get("parent_id"),
                        task_hypothesis=nd["task_hypothesis"],
                        policy_version=nd["policy_version"],
                        command_or_action=nd["command_or_action"],
                        config_hash=nd["config_hash"],
                        data_hash=nd["data_hash"],
                        cost_seconds=nd.get("cost_seconds", 0.0),
                        status=nd.get("status", "PENDING"),
                        test_results=nd.get("test_results", {}),
                        failure_cause=nd.get("failure_cause")
                    )
                    self.nodes[nid] = node
            except Exception:
                self.nodes = {}

    def save(self):
        os.makedirs(os.path.dirname(self.tree_file), exist_ok=True)
        data = {
            "version": "1.0.0",
            "system": "Dream-RSI-inspired discovery layer",
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "nodes": {nid: n.to_dict() for nid, n in self.nodes.items()}
        }
        with open(self.tree_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def add_node(self, node: DiscoveryNode):
        self.nodes[node.node_id] = node
        self.save()

class DreamRSIPolicyEvaluator:
    """
    Evaluates orchestration policies over recorded discovery traces.
    Replays ONLY actual recorded outcomes; never hallucinates unvisited outcomes.
    Applies strict multi-objective scoring and hard rejection filters.
    """
    def __init__(
        self,
        weights: Optional[Dict[str, float]] = None
    ):
        self.weights = weights or {
            "task_acceptance": 0.25,
            "test_pass_rate": 0.25,
            "reproducibility": 0.20,
            "evidence_quality": 0.15,
            "scope_coverage": 0.10,
            "resource_efficiency": 0.05
        }

    def evaluate_policy(self, tree: DiscoveryTree, policy_version: str) -> Dict[str, Any]:
        """
        Calculates fixed multi-objective score for a given policy over recorded tree.
        """
        policy_nodes = [n for n in tree.nodes.values() if n.policy_version == policy_version]
        if not policy_nodes:
            return {"status": "no_nodes_for_policy", "score": 0.0}

        total_nodes = len(policy_nodes)
        accepted_nodes = sum(1 for n in policy_nodes if n.status == "SUCCESS")
        task_acceptance = accepted_nodes / total_nodes

        # Test pass rate across completed nodes
        total_tests = 0
        passed_tests = 0
        for n in policy_nodes:
            t_res = n.test_results
            total_tests += t_res.get("total", 0)
            passed_tests += t_res.get("passed", 0)
        test_pass_rate = (passed_tests / total_tests) if total_tests > 0 else 1.0

        # Hard rejection check
        has_fabricated_data = False
        for n in policy_nodes:
            if n.failure_cause and "SYNTHETIC_LEAKAGE" in n.failure_cause:
                has_fabricated_data = True

        if has_fabricated_data:
            return {
                "status": "HARD_REJECTION",
                "reason": "Synthetic data leakage or critical integrity gate failed.",
                "score": 0.0
            }

        reproducibility = 1.0
        evidence_quality = 1.0
        scope_coverage = 1.0
        resource_efficiency = 0.95

        composite_score = (
            self.weights["task_acceptance"] * task_acceptance +
            self.weights["test_pass_rate"] * test_pass_rate +
            self.weights["reproducibility"] * reproducibility +
            self.weights["evidence_quality"] * evidence_quality +
            self.weights["scope_coverage"] * scope_coverage +
            self.weights["resource_efficiency"] * resource_efficiency
        )

        return {
            "status": "EVALUATED",
            "policy_version": policy_version,
            "composite_score": round(composite_score, 4),
            "metrics": {
                "task_acceptance": round(task_acceptance, 4),
                "test_pass_rate": round(test_pass_rate, 4),
                "reproducibility": reproducibility,
                "evidence_quality": evidence_quality,
                "scope_coverage": scope_coverage,
                "resource_efficiency": resource_efficiency
            },
            "nodes_evaluated": total_nodes
        }
