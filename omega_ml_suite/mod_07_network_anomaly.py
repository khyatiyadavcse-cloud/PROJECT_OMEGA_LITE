"""
Module 07: Network Anomaly Detection Engine
Monitors bandwidth spikes, port activity, packet rates, and unusual connection protocols.
"""

import numpy as np
import pandas as pd

class NetworkAnomalyDetector:
    def __init__(self, normal_bandwidth_mb_min=20.0):
        self.normal_bw = normal_bandwidth_mb_min

    def analyze_network_stream(self, traffic_data=None):
        """
        Input format:
        {
          "bandwidth_mb_min": 450.0,
          "active_ports": [22, 80, 443, 4444, 31337],
          "packet_rate_per_sec": 12500,
          "unique_destinations": 140,
          "unusual_protocol": True
        }
        """
        if traffic_data is None:
            traffic_data = {
                "bandwidth_mb_min": 450.0,
                "active_ports": [22, 80, 443, 4444, 31337],
                "packet_rate_per_sec": 12500,
                "unique_destinations": 140,
                "unusual_protocol": True
            }
            
        anomalies = []
        score = 0
        
        bw = traffic_data.get("bandwidth_mb_min", 20.0)
        if bw > self.normal_bw * 5:
            score += 40
            anomalies.append(f"Bandwidth spike detected ({bw} MB/min vs normal {self.normal_bw} MB/min)")
            
        ports = traffic_data.get("active_ports", [])
        suspicious_ports = [p for p in ports if p in [4444, 31337, 6667, 1337]]
        if suspicious_ports:
            score += 30
            anomalies.append(f"Suspicious port activity detected: {suspicious_ports}")
            
        if traffic_data.get("packet_rate_per_sec", 0) > 5000:
            score += 20
            anomalies.append("Packet frequency surge (potential port scan or exfiltration)")
            
        if traffic_data.get("unusual_protocol", False):
            score += 15
            anomalies.append("Non-standard network protocol observed")
            
        final_score = min(100, score)
        
        return {
            "status": "[!] TRAFFIC ANOMALY DETECTED" if final_score >= 50 else "NORMAL NETWORK TRAFFIC",
            "network_anomaly_score_pct": final_score,
            "detected_anomalies": anomalies,
            "current_metrics": traffic_data
        }
