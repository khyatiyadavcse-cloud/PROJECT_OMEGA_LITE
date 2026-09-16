"""
Synthetic Data Generator for OMEGA ML Suite.
Generates realistic telemetry for assets, login behaviors, vulnerabilities, network traffic, endpoint metrics, cloud configs.
"""

import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_asset_telemetry(n_samples=250, seed=42):
    """Generates synthetic asset telemetry dataset for Risk Prediction & Anomaly Detection."""
    np.random.seed(seed)
    random.seed(seed)
    
    device_names = [f"Finance-PC-{i:02d}" for i in range(1, 30)] + \
                   [f"HR-Server-{i:02d}" for i in range(1, 20)] + \
                   [f"Dev-Workstation-{i:02d}" for i in range(1, 50)] + \
                   [f"Bank-DB-Master-{i:02d}" for i in range(1, 10)] + \
                   [f"App-Server-{i:02d}" for i in range(1, 50)] + \
                   [f"Employee-Laptop-{i:02d}" for i in range(1, 92)]
                   
    criticalities = ["Public PC", "Employee PC", "HR Server", "Finance Server", "Bank Database"]
    
    data = []
    for i in range(n_samples):
        dev = device_names[i % len(device_names)]
        cve_count = np.random.poisson(lam=3)
        cve_max_cvss = min(10.0, round(float(np.random.exponential(scale=3.0)), 1)) if cve_count > 0 else 0.0
        failed_logins = int(np.random.negative_binomial(n=1, p=0.15))
        os_patch_age_days = int(np.random.gamma(shape=2, scale=30))
        software_risk_score = round(float(np.random.uniform(10, 95)), 1)
        behavior_anomaly_score = round(float(np.random.uniform(0, 100)), 1)
        asset_crit_type = random.choice(criticalities)
        
        # Calculate raw synthetic risk label (High: 1, Low/Med: 0)
        risk_raw = (
            cve_max_cvss * 4.0 + 
            min(failed_logins * 3.5, 35) + 
            min(os_patch_age_days * 0.25, 25) + 
            software_risk_score * 0.15 + 
            behavior_anomaly_score * 0.15
        )
        is_high_risk = 1 if risk_raw > 65 else 0
        
        data.append({
            "device_id": dev,
            "cve_max_cvss": cve_max_cvss,
            "failed_logins": failed_logins,
            "os_patch_age_days": os_patch_age_days,
            "software_risk_score": software_risk_score,
            "behavior_anomaly_score": behavior_anomaly_score,
            "asset_criticality_type": asset_crit_type,
            "risk_score_raw": min(100.0, round(risk_raw, 1)),
            "is_high_risk": is_high_risk
        })
        
    return pd.DataFrame(data)

def generate_cve_database(n_cves=500, seed=42):
    """Generates synthetic CVE database with 500 vulnerabilities for AI Vulnerability Intelligence."""
    np.random.seed(seed)
    random.seed(seed)
    
    cves = []
    vendors = ["Apache", "OpenSSL", "Linux Kernel", "Windows OS", "PostgreSQL", "Nginx", "Docker", "Kubernetes"]
    
    for i in range(1, n_cves + 1):
        cve_id = f"CVE-2025-{1000 + i}"
        cvss = round(float(np.random.uniform(2.0, 10.0)), 1)
        exploitability = random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"])
        asset_importance = random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"])
        internet_exposed = random.choice([True, False])
        existing_patch = random.choice([True, False])
        historical_attacks = int(np.random.poisson(lam=5))
        affected_vendor = random.choice(vendors)
        
        cves.append({
            "cve_id": cve_id,
            "vendor": affected_vendor,
            "cvss": cvss,
            "exploitability": exploitability,
            "asset_importance": asset_importance,
            "internet_exposed": internet_exposed,
            "existing_patch": existing_patch,
            "historical_attacks": historical_attacks
        })
        
    return pd.DataFrame(cves)

def generate_uba_telemetry(seed=42):
    """Generates User Behavior Analytics (UBA) dataset."""
    return [
        {
            "user": "Rahul",
            "normal_login_time": "09:10–09:40",
            "normal_device": "Laptop-04",
            "normal_location": "Office (India)",
            "current_login_time": "03:14 AM",
            "current_device": "Unknown Device (Android)",
            "current_ip": "185.220.101.5",
            "current_location": "Foreign IP (Unknown)",
            "failed_logins": 15,
            "session_duration_min": 2
        },
        {
            "user": "Priya",
            "normal_login_time": "10:00–10:30",
            "normal_device": "Desktop-01",
            "normal_location": "Office (India)",
            "current_login_time": "10:05 AM",
            "current_device": "Desktop-01",
            "current_ip": "192.168.1.50",
            "current_location": "Office (India)",
            "failed_logins": 0,
            "session_duration_min": 420
        }
    ]
