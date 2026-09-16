"""
Module 17: Risk + Business Impact Engine
Calculates enterprise composite risk by multiplying technical risk by business asset criticality.
"""

from omega_ml_suite.config import BUSINESS_CRITICALITY

class BusinessImpactEngine:
    def __init__(self):
        self.criticality_map = BUSINESS_CRITICALITY

    def calculate_business_risk(self, asset_name="Bank Database", technical_risk=65, criticality_type="Bank Database"):
        crit_info = self.criticality_map.get(criticality_type, {"multiplier": 1.0, "score": 50})
        multiplier = crit_info["multiplier"]
        
        composite_business_risk = round(technical_risk * multiplier, 1)
        
        return {
            "asset_name": asset_name,
            "technical_risk_score": technical_risk,
            "business_criticality": criticality_type,
            "impact_multiplier": multiplier,
            "composite_business_risk_score": composite_business_risk,
            "soc_priority_level": "P1 - CRITICAL ATTENTION" if composite_business_risk >= 110 else ("P2 - HIGH" if composite_business_risk >= 80 else "P3 - STANDARD"),
            "narrative": f"{asset_name} has a technical risk of {technical_risk} but carries composite business risk of {composite_business_risk} due to criticality multiplier x{multiplier}."
        }
