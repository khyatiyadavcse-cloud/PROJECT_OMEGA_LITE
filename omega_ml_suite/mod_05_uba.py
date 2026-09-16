"""
Module 05: User Behavior Analytics (UBA)
Builds per-user baseline profiles and calculates behavioral risk score deviations.
"""

from omega_ml_suite.data_generator import generate_uba_telemetry

class UserBehaviorAnalytics:
    def __init__(self):
        self.baselines = {
            "Rahul": {
                "normal_login_time": "09:10–09:40",
                "normal_device": "Laptop-04",
                "normal_location": "Office (India)",
                "normal_ip_range": "192.168.1.x"
            }
        }

    def analyze_user_event(self, username="Rahul", current_event=None):
        if current_event is None:
            telemetry = generate_uba_telemetry()
            current_event = [t for t in telemetry if t["user"] == username][0]
            
        baseline = self.baselines.get(username, {
            "normal_login_time": "09:00–17:00",
            "normal_device": "Standard Workstation",
            "normal_location": "Office",
            "normal_ip_range": "Internal"
        })
        
        # Calculate deviation score
        deviations = []
        behavior_risk_points = 0
        
        if "03:" in current_event.get("current_login_time", ""):
            deviations.append("Unusual Login Time (Off-hours)")
            behavior_risk_points += 35
            
        if "Unknown" in current_event.get("current_device", ""):
            deviations.append("Unrecognized Device Hardware")
            behavior_risk_points += 25
            
        if "Foreign" in current_event.get("current_location", "") or "185." in current_event.get("current_ip", ""):
            deviations.append("Anomalous IP Location (Foreign Network)")
            behavior_risk_points += 30
            
        failed = current_event.get("failed_logins", 0)
        if failed > 5:
            deviations.append(f"High Failed Login Rate ({failed} attempts)")
            behavior_risk_points += 25
            
        final_risk = min(100, behavior_risk_points)
        
        return {
            "user": username,
            "baseline": baseline,
            "current_activity": {
                "login_time": current_event.get("current_login_time"),
                "device": current_event.get("current_device"),
                "ip": current_event.get("current_ip"),
                "location": current_event.get("current_location")
            },
            "behavioral_risk_score": final_risk,
            "behavioral_risk_trend": "^ HIGH RISK ELEVATION" if final_risk >= 60 else "-> STABLE",
            "detected_deviations": deviations
        }
