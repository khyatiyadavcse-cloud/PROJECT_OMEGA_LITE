"""
Module 29: AI-Generated Natural Language Risk Narrative Engine
Generates clear human-readable narrative explanations for asset risk profiles.
"""

class RiskNarrativeGenerator:
    def __init__(self):
        pass

    def generate_narrative(self, asset_id="Finance-PC-07", risk_score=87, cve_severity="high", patch_status="outdated", failed_logins=18):
        narrative = (
            f"{asset_id} is currently classified as HIGH RISK (Score: {risk_score}/100) because "
            f"it contains a {cve_severity}-severity vulnerability, has not received recent OS patches ({patch_status}), "
            f"and shows an unusual increase in failed authentication attempts ({failed_logins} attempts)."
        )
        return {
            "asset_id": asset_id,
            "risk_score": risk_score,
            "risk_narrative": narrative
        }
