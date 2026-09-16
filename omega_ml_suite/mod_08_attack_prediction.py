"""
Module 08: Attack Path Simulation & Attack Prediction Engine
Simulates multi-hop lateral movement pathways and predicts attack probability.
"""

class AttackPathSimulator:
    def __init__(self):
        pass

    def simulate_attack_path(self, entry_point="Asset A", target="Database"):
        """
        Simulates:
        Asset A -> Weak Password -> Server B -> Critical Vulnerability -> Database
        """
        hops = [
            {"step": 1, "node": entry_point, "vulnerability": "Exposed SSH / Weak Password", "compromise_prob": 0.85},
            {"step": 2, "node": "Server B (App Gateway)", "vulnerability": "Unpatched CVE-2025-1042", "compromise_prob": 0.90},
            {"step": 3, "node": target, "vulnerability": "Hardcoded DB Credentials in App Config", "compromise_prob": 0.95}
        ]
        
        # Cumulative path risk
        path_risk = 1.0
        for h in hops:
            path_risk *= h["compromise_prob"]
            
        path_risk_pct = int(round(path_risk * 100))
        
        return {
            "entry_asset": entry_point,
            "target_asset": target,
            "simulated_hops": hops,
            "overall_attack_path_risk": "HIGH" if path_risk_pct >= 70 else "MEDIUM",
            "path_compromise_probability_pct": path_risk_pct,
            "summary_narrative": f"Simulated attack path reveals high risk from {entry_point} through Server B to {target} due to chained vulnerabilities."
        }
