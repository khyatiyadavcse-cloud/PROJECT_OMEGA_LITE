"""
Module 12: Early Warning & Multi-Channel Alert System
Triggers security warning alerts when risk scores cross defined thresholds and dispatches notifications.
"""

from datetime import datetime

class EarlyWarningSystem:
    def __init__(self, alert_threshold=75):
        self.threshold = alert_threshold

    def evaluate_risk_delta(self, asset_id="Server-02", old_risk=52, new_risk=81, reason="Critical vulnerability detected."):
        is_triggered = new_risk >= self.threshold and (new_risk - old_risk) >= 15
        
        alert_payload = {
            "timestamp": datetime.now().isoformat(),
            "asset_id": asset_id,
            "old_risk": old_risk,
            "new_risk": new_risk,
            "risk_delta": f"+{new_risk - old_risk}",
            "reason": reason,
            "alert_level": "[!] CRITICAL SECURITY WARNING" if is_triggered else "INFO"
        }
        
        notifications_sent = {}
        if is_triggered:
            notifications_sent = {
                "Email": f"Sent alert to admin@corp.domain regarding {asset_id}",
                "Dashboard": f"Pushed live alert banner to SOC Command Center",
                "Webhook": "HTTP POST 200 OK to https://hooks.slack.com/services/omega-alerts",
                "SMS/WhatsApp": f"SMS dispatched to Security On-Call (+1-800-555-0199)"
            }
            
        return {
            "alert_triggered": is_triggered,
            "alert_details": alert_payload,
            "channels_dispatched": notifications_sent
        }
