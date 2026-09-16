"""
Module 06: Account Takeover (ATO) Detection Engine
Detects compromised user accounts and produces automated mitigation recommendations.
"""

class AccountTakeoverDetector:
    def __init__(self):
        pass

    def evaluate_account(self, login_stats):
        """
        Input format:
        {
          "normal_logins_per_day": 5,
          "today_logins": 47,
          "failed_attempts": 12,
          "is_new_ip": True,
          "is_new_device": True,
          "is_unusual_time": True
        }
        """
        score = 0
        factors = []
        
        logins_ratio = login_stats.get("today_logins", 0) / max(1, login_stats.get("normal_logins_per_day", 5))
        if logins_ratio >= 5.0:
            score += 30
            factors.append(f"Abnormal login frequency ({login_stats['today_logins']} attempts vs 5 avg)")
            
        if login_stats.get("failed_attempts", 0) >= 10:
            score += 25
            factors.append(f"{login_stats['failed_attempts']} failed authentication attempts")
            
        if login_stats.get("is_new_ip", False):
            score += 15
            factors.append("Authentication from unfamiliar IP address")
            
        if login_stats.get("is_new_device", False):
            score += 15
            factors.append("Authentication from unseen device fingerprint")
            
        if login_stats.get("is_unusual_time", False):
            score += 15
            factors.append("Access during anomalous off-duty hours")
            
        ato_probability = min(99, score)
        is_compromised = ato_probability >= 75
        
        recommendations = [
            "Force immediate logout across all active sessions",
            "Require mandatory password reset",
            "Enforce Multi-Factor Authentication (MFA)",
            "Temporarily block suspicious IP / session token"
        ] if is_compromised else ["Monitor account session logs"]
        
        return {
            "account_status": "POTENTIALLY COMPROMISED" if is_compromised else "SECURE",
            "ato_probability_pct": ato_probability,
            "risk_factors": factors,
            "automated_recommendations": recommendations
        }
