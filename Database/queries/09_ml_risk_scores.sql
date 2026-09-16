-- ========================================================
-- OMEGA ML SUITE: AUTOMATED RISK SCORE SEED DATA
-- Generated for Database Integration
-- ========================================================

CREATE TABLE IF NOT EXISTS asset_ml_risk_scores (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(100) NOT NULL,
    cve_max_cvss NUMERIC(3,1),
    failed_logins INT,
    os_patch_age_days INT,
    software_risk_score NUMERIC(4,1),
    behavior_anomaly_score NUMERIC(4,1),
    asset_criticality VARCHAR(50),
    risk_score NUMERIC(4,1),
    is_high_risk INT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

TRUNCATE TABLE asset_ml_risk_scores;

INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-01', 0.5, 1, 30, 35.9, 52.5, 'Public PC', 26.3, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-02', 1.0, 2, 32, 60.4, 4.6, 'Public PC', 28.8, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-03', 8.9, 23, 62, 20.4, 49.5, 'HR Server', 96.6, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-04', 0.0, 11, 29, 54.2, 54.7, 'Employee PC', 58.6, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-05', 0.7, 0, 11, 40.3, 28.1, 'Employee PC', 15.8, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-06', 10.0, 6, 26, 19.8, 86.3, 'Employee PC', 83.4, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-07', 1.1, 4, 97, 75.5, 49.4, 'Public PC', 61.4, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-08', 0.3, 0, 87, 53.2, 90.8, 'Bank Database', 44.5, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-09', 0.2, 2, 94, 25.9, 89.3, 'Public PC', 48.6, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-10', 0.8, 2, 63, 45.5, 22.2, 'Bank Database', 36.1, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-11', 8.6, 5, 6, 13.1, 61.0, 'Finance Server', 64.5, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-12', 1.0, 10, 48, 93.8, 24.2, 'Public PC', 68.7, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-13', 3.0, 4, 53, 11.4, 51.2, 'Public PC', 48.6, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-14', 3.5, 2, 32, 88.6, 87.7, 'Public PC', 55.4, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-15', 0.8, 2, 15, 86.3, 88.7, 'Employee PC', 40.2, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-16', 0.5, 14, 14, 66.4, 0.5, 'Employee PC', 50.5, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-17', 0.8, 8, 22, 43.4, 89.2, 'Bank Database', 56.6, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-18', 3.8, 0, 24, 25.1, 94.0, 'Bank Database', 39.1, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-19', 7.9, 6, 58, 69.2, 57.0, 'Public PC', 86.0, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-20', 2.2, 14, 15, 40.6, 29.4, 'Bank Database', 58.0, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-21', 4.8, 11, 56, 49.6, 54.3, 'Employee PC', 83.8, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-22', 0.1, 7, 23, 56.0, 63.7, 'Bank Database', 48.6, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-23', 1.7, 0, 25, 23.3, 25.0, 'Finance Server', 20.3, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-24', 2.8, 3, 145, 13.9, 4.1, 'Employee PC', 49.4, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-25', 2.0, 3, 34, 63.2, 50.3, 'Finance Server', 44.0, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-26', 3.1, 0, 55, 58.9, 38.8, 'Bank Database', 40.8, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-27', 0.2, 0, 61, 37.1, 84.5, 'HR Server', 34.3, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-28', 0.0, 13, 29, 39.0, 93.1, 'Public PC', 62.1, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Finance-PC-29', 7.0, 4, 63, 58.7, 63.2, 'Employee PC', 76.0, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-01', 3.3, 7, 45, 20.0, 14.3, 'Finance Server', 54.1, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-02', 0.3, 4, 109, 93.8, 75.3, 'HR Server', 65.6, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-03', 4.5, 4, 33, 14.8, 11.9, 'HR Server', 44.3, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-04', 9.8, 2, 52, 16.3, 55.4, 'Employee PC', 70.0, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-05', 6.9, 0, 98, 85.7, 45.6, 'Employee PC', 71.8, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-06', 1.9, 1, 64, 79.2, 68.5, 'HR Server', 49.3, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-07', 8.1, 3, 163, 78.9, 98.7, 'Public PC', 94.5, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-08', 10.0, 14, 10, 83.5, 81.3, 'Public PC', 100.0, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-09', 0.4, 19, 30, 62.5, 35.8, 'Finance Server', 58.8, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-10', 4.4, 5, 132, 21.6, 1.5, 'Public PC', 63.6, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-11', 7.0, 4, 92, 22.5, 92.7, 'HR Server', 82.3, 1);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-12', 1.2, 2, 65, 39.4, 89.7, 'HR Server', 47.4, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-13', 0.1, 0, 21, 17.5, 12.1, 'Bank Database', 10.1, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-14', 2.1, 5, 45, 73.6, 18.5, 'HR Server', 51.0, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-15', 2.9, 2, 41, 70.6, 89.5, 'Public PC', 52.9, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-16', 1.8, 3, 19, 20.2, 89.1, 'Finance Server', 38.8, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-17', 2.3, 4, 28, 58.5, 35.6, 'Bank Database', 44.3, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-18', 0.5, 0, 30, 86.2, 8.0, 'Public PC', 23.6, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('HR-Server-19', 1.5, 25, 23, 24.5, 66.9, 'Finance Server', 60.5, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Dev-Workstation-01', 1.2, 2, 11, 23.1, 48.1, 'Public PC', 25.2, 0);
INSERT INTO asset_ml_risk_scores (device_id, cve_max_cvss, failed_logins, os_patch_age_days, software_risk_score, behavior_anomaly_score, asset_criticality, risk_score, is_high_risk) VALUES ('Dev-Workstation-02', 1.2, 0, 87, 37.4, 81.0, 'Bank Database', 44.3, 0);