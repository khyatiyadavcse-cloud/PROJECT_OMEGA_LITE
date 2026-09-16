"""
Module 28: Real-Time Event Streaming Simulator
Simulates a live event stream (Kafka / WebSocket queue) updating risk scores in real-time.
"""

import time
import random
from datetime import datetime

class RealTimeStreamSimulator:
    def __init__(self):
        pass

    def stream_events(self, asset_id="Finance-PC-01", n_ticks=4):
        """Simulates live event stream ticks pushing risk score updates."""
        current_score = 42
        ticks = [
            {"time": datetime.now().strftime("%H:%M:%S"), "score": 42, "event": "Stream initialized (Baseline)"}
        ]
        
        increments = [
            (7, "Failed login attempt ingested via syslog"),
            (18, "CVE-2025-1042 vulnerability matched to device inventory"),
            (14, "Unusual location access anomaly detected")
        ]
        
        for idx in range(min(n_ticks - 1, len(increments))):
            inc, evt = increments[idx]
            current_score += inc
            ticks.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "score": current_score,
                "event": evt
            })
            
        return {
            "asset_id": asset_id,
            "streaming_protocol": "Simulated WebSocket / Kafka Stream",
            "score_progression": [t["score"] for t in ticks],
            "stream_ticks": ticks
        }
