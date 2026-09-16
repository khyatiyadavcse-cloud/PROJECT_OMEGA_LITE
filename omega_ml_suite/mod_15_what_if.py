"""
Module 15: What-If Risk Simulator
Simulates the preventive impact of security controls (MFA, Patching, Password Strength) on asset risk.
"""

class WhatIfRiskSimulator:
    def __init__(self):
        pass

    def simulate_controls(self, initial_risk=91, apply_mfa=True, apply_patch=True, apply_strong_password=True):
        """
        Calculates risk delta:
        Before: Password Weak, MFA OFF, Patch Missing -> Risk 91
        Enable MFA (-18), Install Patch (-24), Strong Password (-11)
        Predicted Risk: 91 -> 38
        """
        current_risk = initial_risk
        applied_remediations = []
        
        if apply_patch:
            current_risk -= 24
            applied_remediations.append({"control": "Install Critical OS & Software Patch", "risk_reduction": -24})
            
        if apply_mfa:
            current_risk -= 18
            applied_remediations.append({"control": "Enforce Multi-Factor Authentication (MFA)", "risk_reduction": -18})
            
        if apply_strong_password:
            current_risk -= 11
            applied_remediations.append({"control": "Upgrade to Enterprise Strong Password Policy", "risk_reduction": -11})
            
        predicted_risk = max(5, current_risk)
        
        return {
            "initial_risk_score": initial_risk,
            "predicted_risk_score": predicted_risk,
            "total_risk_reduction": initial_risk - predicted_risk,
            "applied_controls": applied_remediations,
            "simulation_narrative": f"Applying selected controls reduces asset risk from {initial_risk} down to {predicted_risk} (-{initial_risk - predicted_risk} points)."
        }
