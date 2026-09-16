"""
Module 27: Feature Engineering Pipeline Layer
Transforms raw telemetry signals into domain-specific cyber risk features.
"""

import numpy as np
import pandas as pd

class FeatureEngineeringPipeline:
    def __init__(self):
        pass

    def transform_raw_telemetry(self, raw_data):
        """
        Input raw_data format:
        {
          "failed_login_count": 15,
          "avg_daily_attempts": 3,
          "cve_count": 8,
          "installed_software_count": 25,
          "os_patch_age_days": 180,
          "exposed_services_count": 5
        }
        """
        failed_cnt = raw_data.get("failed_login_count", 0)
        avg_attempts = max(1, raw_data.get("avg_daily_attempts", 1))
        
        # 1. Failed login rate
        failed_login_rate = round(failed_cnt / avg_attempts, 2)
        
        # 2. Vulnerability density
        cve_cnt = raw_data.get("cve_count", 0)
        sw_cnt = max(1, raw_data.get("installed_software_count", 1))
        vuln_density = round(cve_cnt / sw_cnt, 2)
        
        # 3. Patch age risk factor
        patch_age = raw_data.get("os_patch_age_days", 0)
        patch_age_factor = round(min(1.0, patch_age / 180.0), 2)
        
        # 4. Service exposure index
        exposed_services = raw_data.get("exposed_services_count", 0)
        exposure_index = round(min(1.0, exposed_services / 10.0), 2)
        
        engineered_features = {
            "failed_login_rate": failed_login_rate,
            "vulnerability_density": vuln_density,
            "patch_age_factor": patch_age_factor,
            "exposure_index": exposure_index,
            "composite_threat_density": round((failed_login_rate + vuln_density * 5 + patch_age_factor * 3) / 9.0, 2)
        }
        
        return {
            "raw_inputs": raw_data,
            "engineered_features": engineered_features
        }
