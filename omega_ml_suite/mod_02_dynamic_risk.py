"""
Module 02: Dynamic Risk Score & Explainable Scoring Layer
Implements continuous temporal risk score tracking and formula-based explainability:
RiskScore = w1*V + w2*L + w3*P + w4*S + w5*B + w6*A
"""

import pandas as pd
from omega_ml_suite.config import RISK_WEIGHTS

class DynamicRiskEngine:
    def __init__(self, weights=None):
        self.weights = weights or RISK_WEIGHTS

    def calculate_explainable_score(self, V, L, P, S, B, A):
        """
        Calculates exact formula score:
        RiskScore = w1*V + w2*L + w3*P + w4*S + w5*B + w6*A
        All inputs scaled 0..100
        """
        w = self.weights
        score = (
            w["vulnerability_severity"] * V +
            w["login_anomalies"] * L +
            w["patch_status"] * P +
            w["software_risk"] * S +
            w["behavioral_anomaly"] * B +
            w["asset_criticality"] * A
        )
        
        breakdown = {
            "vulnerability_contrib (V)": round(w["vulnerability_severity"] * V, 1),
            "login_anomalies_contrib (L)": round(w["login_anomalies"] * L, 1),
            "patch_status_contrib (P)": round(w["patch_status"] * P, 1),
            "software_risk_contrib (S)": round(w["software_risk"] * S, 1),
            "behavioral_anomaly_contrib (B)": round(w["behavioral_anomaly"] * B, 1),
            "asset_criticality_contrib (A)": round(w["asset_criticality"] * A, 1),
        }
        
        return {
            "formula_score": round(score, 1),
            "breakdown": breakdown
        }

    def generate_timeline(self, device_id="Finance-PC-01"):
        """Generates dynamic risk score progression over time."""
        timeline = [
            {"time": "09:00", "score": 42, "reason": "Baseline start"},
            {"time": "10:00", "score": 51, "reason": "Failed login attempt detected (+9)"},
            {"time": "11:00", "score": 67, "reason": "New critical CVE released (+16)"},
            {"time": "12:00", "score": 83, "reason": "Unusual login location detected (+16)"}
        ]
        return {
            "device_id": device_id,
            "timeline": timeline,
            "current_score": 83
        }
