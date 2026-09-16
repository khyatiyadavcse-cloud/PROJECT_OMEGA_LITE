"""
Module 18: Password Risk ML Analyzer
Evaluates password security risk from password metadata without storing actual plaintext passwords.
"""

class PasswordRiskAnalyzer:
    def __init__(self):
        pass

    def evaluate_password_metadata(self, length=7, has_uppercase=False, has_digits=True, has_special=False, age_days=180, breach_exposure_count=3, reuse_count=2):
        """
        Evaluates password metadata securely.
        """
        score = 0
        risk_factors = []
        
        if length < 10:
            score += 35
            risk_factors.append(f"Short length ({length} chars < 10 min requirement)")
            
        if not (has_uppercase and has_digits and has_special):
            score += 20
            risk_factors.append("Low character diversity (missing upper/special chars)")
            
        if age_days > 90:
            score += 20
            risk_factors.append(f"Password age expired ({age_days} days old > 90 days max)")
            
        if breach_exposure_count > 0:
            score += 15
            risk_factors.append(f"Exposed in {breach_exposure_count} public breach metadata logs")
            
        if reuse_count > 0:
            score += 10
            risk_factors.append(f"Password pattern reused across {reuse_count} internal accounts")
            
        password_risk_pct = min(100, score)
        
        return {
            "password_risk_pct": password_risk_pct,
            "risk_classification": "CRITICAL" if password_risk_pct >= 75 else ("HIGH" if password_risk_pct >= 50 else "LOW"),
            "detected_risk_factors": risk_factors,
            "security_compliance": "NON-COMPLIANT" if password_risk_pct >= 50 else "COMPLIANT"
        }
