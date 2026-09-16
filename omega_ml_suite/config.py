"""
Configuration and constants for OMEGA ML Suite.
"""

# Risk Scoring Weights for: RiskScore = w1*V + w2*L + w3*P + w4*S + w5*B + w6*A
RISK_WEIGHTS = {
    "vulnerability_severity": 0.25, # V
    "login_anomalies": 0.20,        # L
    "patch_status": 0.15,           # P
    "software_risk": 0.15,          # S
    "behavioral_anomaly": 0.15,     # B
    "asset_criticality": 0.10       # A
}

# Risk Thresholds
CRITICAL_RISK_THRESHOLD = 80.0
HIGH_RISK_THRESHOLD = 65.0
MEDIUM_RISK_THRESHOLD = 40.0

# Asset Criticality Weight Multipliers
BUSINESS_CRITICALITY = {
    "Public PC": {"multiplier": 1.0, "score": 25},
    "Employee PC": {"multiplier": 1.2, "score": 50},
    "HR Server": {"multiplier": 1.6, "score": 85},
    "Finance Server": {"multiplier": 1.8, "score": 90},
    "Bank Database": {"multiplier": 2.0, "score": 100},
}
