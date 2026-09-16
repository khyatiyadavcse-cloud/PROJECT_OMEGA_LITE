"""
Module 21: Identity & Access Management (IAM) Risk Analyzer
Evaluates privilege risks, dormant admin accounts, and access policy violations.
"""

class IdentityAccessRiskAnalyzer:
    def __init__(self):
        pass

    def evaluate_identity_risk(self, identity_data=None):
        """
        Input format:
        {
          "username": "admin_svc_01",
          "is_admin": True,
          "is_inactive_90d": False,
          "excessive_permissions_count": 14,
          "unusual_login_flag": True,
          "new_device_flag": True
        }
        """
        if identity_data is None:
            identity_data = {
                "username": "admin_svc_01",
                "is_admin": True,
                "is_inactive_90d": False,
                "excessive_permissions_count": 14,
                "unusual_login_flag": True,
                "new_device_flag": True
            }
            
        score = 0
        reasons = []
        
        if identity_data.get("is_admin", False):
            score += 25
            reasons.append("High Privileged Admin Account")
            
        if identity_data.get("unusual_login_flag", False):
            score += 25
            reasons.append("Unusual Login Event")
            
        if identity_data.get("new_device_flag", False):
            score += 20
            reasons.append("Unverified New Device")
            
        excess = identity_data.get("excessive_permissions_count", 0)
        if excess > 5:
            score += 18
            reasons.append(f"{excess} unused excessive RBAC permissions")
            
        user_risk = min(100, score)
        
        return {
            "username": identity_data.get("username"),
            "user_risk_score": user_risk,
            "risk_classification": "HIGH IAM RISK" if user_risk >= 70 else "LOW IAM RISK",
            "combined_reasons": " + ".join(reasons)
        }
