"""
Module 03: AI Vulnerability Intelligence & CVE Prioritization
Analyzes 500+ CVEs, predicts priority, and isolates top 10 actionable vulnerabilities.
"""

import pandas as pd
import numpy as np
from omega_ml_suite.data_generator import generate_cve_database

class VulnerabilityIntelligenceEngine:
    def __init__(self):
        pass

    def prioritize_vulnerabilities(self, cve_df=None, top_n=10):
        if cve_df is None:
            cve_df = generate_cve_database(n_cves=500)
            
        df = cve_df.copy()
        
        # Priority Scoring Model
        exploit_map = {"LOW": 1.0, "MEDIUM": 2.0, "HIGH": 3.5, "CRITICAL": 5.0}
        asset_map = {"LOW": 1.0, "MEDIUM": 2.0, "HIGH": 3.0, "CRITICAL": 4.0}
        
        df["exploit_val"] = df["exploitability"].map(exploit_map)
        df["asset_val"] = df["asset_importance"].map(asset_map)
        df["internet_val"] = df["internet_exposed"].apply(lambda x: 2.5 if x else 1.0)
        df["patch_val"] = df["existing_patch"].apply(lambda x: 0.5 if x else 2.0)
        
        # Calculate AI Vulnerability Priority Score
        df["ai_priority_score"] = (
            df["cvss"] * 3.0 +
            df["exploit_val"] * 4.0 +
            df["asset_val"] * 3.0 +
            df["internet_val"] * 5.0 +
            df["patch_val"] * 3.0 +
            np.log1p(df["historical_attacks"]) * 2.5
        )
        
        df = df.sort_values(by="ai_priority_score", ascending=False).reset_index(drop=True)
        top_cves = df.head(top_n)
        
        results = []
        for idx, row in top_cves.iterrows():
            ai_priority = "CRITICAL" if row["cvss"] >= 8.5 else ("HIGH" if row["cvss"] >= 7.0 else "MEDIUM")
            action = "Patch immediately" if not row["existing_patch"] else "Apply compensating control"
            results.append({
                "rank": idx + 1,
                "cve_id": row["cve_id"],
                "cvss": row["cvss"],
                "exploitability": row["exploitability"],
                "affected_asset": f"{row['vendor']} Server",
                "ai_priority": ai_priority,
                "ai_score": round(row["ai_priority_score"], 1),
                "recommended_action": action
            })
            
        return {
            "total_analyzed": len(df),
            "top_prioritized_count": top_n,
            "top_vulnerabilities": results
        }
