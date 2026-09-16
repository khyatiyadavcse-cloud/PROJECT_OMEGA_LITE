"""
Module 33: Database Integration & SQL Exporter
Maps ML risk predictions to database tables and generates SQL insert statements for DB sync.
"""

import os
import pandas as pd
from omega_ml_suite.data_generator import generate_asset_telemetry

class DatabaseConnector:
    def __init__(self, output_sql_path=None):
        if output_sql_path is None:
            self.output_sql_path = os.path.join(
                os.path.dirname(__file__), "..", "Database", "queries", "09_ml_risk_scores.sql"
            )
        else:
            self.output_sql_path = output_sql_path

    def export_ml_scores_to_sql(self, telemetry_df=None):
        """Generates SQL insertion statements mapping ML risk scores into the OMEGA database schema."""
        if telemetry_df is None:
            telemetry_df = generate_asset_telemetry(n_samples=50)
            
        lines = [
            "-- ========================================================",
            "-- OMEGA ML SUITE: AUTOMATED RISK SCORE SEED DATA",
            "-- Generated for Database Integration",
            "-- ========================================================\n",
            "CREATE TABLE IF NOT EXISTS asset_ml_risk_scores (",
            "    id SERIAL PRIMARY KEY,",
            "    device_id VARCHAR(100) NOT NULL,",
            "    cve_max_cvss NUMERIC(3,1),",
            "    failed_logins INT,",
            "    os_patch_age_days INT,",
            "    software_risk_score NUMERIC(4,1),",
            "    behavior_anomaly_score NUMERIC(4,1),",
            "    asset_criticality VARCHAR(50),",
            "    risk_score NUMERIC(4,1),",
            "    is_high_risk INT,",
            "    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
            ");\n",
            "TRUNCATE TABLE asset_ml_risk_scores;\n"
        ]
        
        for _, row in telemetry_df.iterrows():
            sql = (
                f"INSERT INTO asset_ml_risk_scores "
                f"(device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) "
                f"VALUES ('{row['device_id']}', {row['cve_max_cvss']}, {row['failed_logins']}, {row['os_patch_age_days']}, {row['software_risk_score']}, {row['behavior_anomaly_score']}, '{row['asset_criticality_type']}', {row['risk_score_raw']}, {row['is_high_risk']});"
            )
            lines.append(sql)
            
        os.makedirs(os.path.dirname(self.output_sql_path), exist_ok=True)
        with open(self.output_sql_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
            
        return {
            "status": "SQL EXPORT SUCCESSFUL",
            "records_exported": len(telemetry_df),
            "sql_file_path": self.output_sql_path
        }
