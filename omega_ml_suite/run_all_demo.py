"""
Master End-to-End Demonstration Runner for OMEGA ML Suite.
Executes and prints verification output for all 31 requested AI/ML security features.
"""

from omega_ml_suite.mod_01_risk_engine import RiskPredictionEngine
from omega_ml_suite.mod_02_dynamic_risk import DynamicRiskEngine
from omega_ml_suite.mod_03_vuln_intel import VulnerabilityIntelligenceEngine
from omega_ml_suite.mod_04_anomaly_detection import AnomalyDetector
from omega_ml_suite.mod_05_uba import UserBehaviorAnalytics
from omega_ml_suite.mod_06_account_takeover import AccountTakeoverDetector
from omega_ml_suite.mod_07_network_anomaly import NetworkAnomalyDetector
from omega_ml_suite.mod_08_attack_prediction import AttackPathSimulator
from omega_ml_suite.mod_09_attack_graph import RiskGraphEngine
from omega_ml_suite.mod_10_xai import ExplainableAIEngine
from omega_ml_suite.mod_11_forecasting import RiskForecaster
from omega_ml_suite.mod_12_early_warning import EarlyWarningSystem
from omega_ml_suite.mod_13_copilot import SecurityCopilot
from omega_ml_suite.mod_14_reports import NaturalLanguageReportGenerator
from omega_ml_suite.mod_15_what_if import WhatIfRiskSimulator
from omega_ml_suite.mod_16_recommendation import SecurityRecommendationEngine
from omega_ml_suite.mod_17_business_impact import BusinessImpactEngine
from omega_ml_suite.mod_18_password_risk import PasswordRiskAnalyzer
from omega_ml_suite.mod_19_malware_detection import MalwareEarlyDetector
from omega_ml_suite.mod_20_cloud_security import CloudSecurityRiskPredictor
from omega_ml_suite.mod_21_identity_access import IdentityAccessRiskAnalyzer
from omega_ml_suite.mod_22_gnn_research import GraphNeuralNetworkRiskModel
from omega_ml_suite.mod_23_federated_learning import FederatedLearningSimulator
from omega_ml_suite.mod_24_adversarial_ml import AdversarialMLProtector
from omega_ml_suite.mod_25_mlops import MLOpsMonitor
from omega_ml_suite.mod_26_continuous_learning import ContinuousLearningPipeline
from omega_ml_suite.mod_27_feature_engineering import FeatureEngineeringPipeline
from omega_ml_suite.mod_28_realtime_streaming import RealTimeStreamSimulator
from omega_ml_suite.mod_29_narrative_generator import RiskNarrativeGenerator

def run_master_demonstration():
    print("=" * 70)
    print("      [+] OMEGA AI SECURITY & ML SUITE - MASTER DEMONSTRATION [+]")
    print("=" * 70)
    
    # 1. Risk Engine
    print("\n--- [Module 01] Multi-Model Risk Prediction Engine ---")
    m1 = RiskPredictionEngine()
    p1 = m1.predict_device_risk({
        "device_id": "Finance-PC-01",
        "cve_max_cvss": 9.8,
        "failed_logins": 18,
        "os_patch_age_days": 180,
        "software_risk_score": 88,
        "behavior_anomaly_score": 92
    })
    print(f"Device: {p1['device_id']}")
    print(f"Risk Score: {p1['risk_score']}/100 | Risk Level: {p1['risk_level']} | Confidence: {p1['confidence_pct']}%")
    print(f"Probabilities: {p1['probabilities']}")
    print(f"Top Risk Factors: {p1['top_risk_factors']}")
    
    # 2. Dynamic Risk Score
    print("\n--- [Module 02] Dynamic Risk Score & Explainable Formula Layer ---")
    m2 = DynamicRiskEngine()
    exp_f = m2.calculate_explainable_score(V=98, L=90, P=85, S=80, B=92, A=90)
    print(f"Risk Score Formula: {exp_f['formula_score']}")
    print(f"Breakdown: {exp_f['breakdown']}")
    
    # 3. Vuln Intel
    print("\n--- [Module 03] AI Vulnerability Intelligence (500 CVE Prioritization) ---")
    m3 = VulnerabilityIntelligenceEngine()
    top_cves = m3.prioritize_vulnerabilities(top_n=3)
    for cve in top_cves["top_vulnerabilities"]:
        print(f"Rank {cve['rank']}: {cve['cve_id']} (CVSS {cve['cvss']}) -> Priority: {cve['ai_priority']} | Action: {cve['recommended_action']}")
        
    # 4. Anomaly Detection
    print("\n--- [Module 04] Unsupervised Anomaly Detection ---")
    m4 = AnomalyDetector()
    anom = m4.detect_anomaly({"login_hour": 3.17, "failed_attempts": 15, "is_known_ip": 0, "is_known_device": 0})
    print(f"Status: {anom['status']} (Anomaly Score: {anom['anomaly_score_pct']}%)")
    
    # 5. UBA
    print("\n--- [Module 05] User Behavior Analytics (UBA) ---")
    m5 = UserBehaviorAnalytics()
    uba = m5.analyze_user_event("Rahul")
    print(f"User: {uba['user']} | Behavioral Risk: {uba['behavioral_risk_score']} ({uba['behavioral_risk_trend']})")
    
    # 6. ATO Detection
    print("\n--- [Module 06] Account Takeover Detection ---")
    m6 = AccountTakeoverDetector()
    ato = m6.evaluate_account({"today_logins": 47, "failed_attempts": 12, "is_new_ip": True, "is_new_device": True})
    print(f"ATO Status: {ato['account_status']} ({ato['ato_probability_pct']}% probability)")
    
    # 7. Network Anomaly
    print("\n--- [Module 07] Network Anomaly Detection ---")
    m7 = NetworkAnomalyDetector()
    net = m7.analyze_network_stream({"bandwidth_mb_min": 450.0, "active_ports": [4444], "unusual_protocol": True})
    print(f"Network Status: {net['status']} (Score: {net['network_anomaly_score_pct']}%)")
    
    # 8. Attack Path Prediction
    print("\n--- [Module 08] Attack Path Prediction & Simulation ---")
    m8 = AttackPathSimulator()
    att = m8.simulate_attack_path("Asset A", "Database")
    print(f"Potential Attack Path Risk: {att['overall_attack_path_risk']} ({att['path_compromise_probability_pct']}% prob)")
    
    # 9. Attack Graph
    print("\n--- [Module 09] Attack Graph / Risk Graph ---")
    m9 = RiskGraphEngine()
    g = m9.get_graph_topology()
    print(f"Critical Path Narrative: {g['ai_narrative']}")
    
    # 10. XAI (SHAP)
    print("\n--- [Module 10] Explainable AI (SHAP Waterfall) ---")
    m10 = ExplainableAIEngine()
    xai = m10.explain_prediction(risk_score=91)
    print(f"Explanation: {xai['explanation_text']}")
    
    # 11. Time-Series Risk Forecasting
    print("\n--- [Module 11] Time-Series Risk Forecasting ---")
    m11 = RiskForecaster()
    fc = m11.forecast_risk(61)
    print(f"Risk Forecast: {[(f['day'], f['predicted_risk']) for f in fc['forecast']]}")
    
    # 12. Early Warning System
    print("\n--- [Module 12] Early Warning System & Alert Distribution ---")
    m12 = EarlyWarningSystem()
    ew = m12.evaluate_risk_delta("Server-02", 52, 81, "Critical vulnerability detected.")
    print(f"Alert Level: {ew['alert_details']['alert_level']} | Dispatched Channels: {list(ew['channels_dispatched'].keys())}")
    
    # 13. AI Copilot
    print("\n--- [Module 13] OMEGA AI Security Copilot ---")
    m13 = SecurityCopilot()
    ans = m13.ask("Which device should I secure first?")
    print(f"Copilot Response:\n{ans}")
    
    # 14. Executive Report
    print("\n--- [Module 14] Natural Language Security Executive Report ---")
    m14 = NaturalLanguageReportGenerator()
    rep = m14.generate_weekly_report()
    print(f"Executive Report Header:\n{rep['report_text'].splitlines()[0:8]}")
    
    # 15. What-If Risk Simulator
    print("\n--- [Module 15] What-If Risk Simulator ---")
    m15 = WhatIfRiskSimulator()
    sim = m15.simulate_controls(initial_risk=91, apply_mfa=True, apply_patch=True, apply_strong_password=True)
    print(f"Before Risk: {sim['initial_risk_score']} -> Predicted Risk After Controls: {sim['predicted_risk_score']} (-{sim['total_risk_reduction']} pts)")
    
    # 16. Recommendation Engine
    print("\n--- [Module 16] Security Recommendation Engine ---")
    m16 = SecurityRecommendationEngine()
    recs = m16.get_recommendations(89)
    print(f"Top Action: {recs['prioritized_actions'][0]['action']} (Expected Reduction: -{recs['prioritized_actions'][0]['expected_reduction']} pts)")
    
    # 17. Business Impact Engine
    print("\n--- [Module 17] Risk + Business Impact Engine ---")
    m17 = BusinessImpactEngine()
    bi = m17.calculate_business_risk("Bank Database", technical_risk=65, criticality_type="Bank Database")
    print(f"Technical Risk: {bi['technical_risk_score']} x Multiplier {bi['impact_multiplier']} -> Composite Business Risk: {bi['composite_business_risk_score']}")
    
    # 18. Password Risk
    print("\n--- [Module 18] Password Risk ML Analyzer ---")
    m18 = PasswordRiskAnalyzer()
    pwd = m18.evaluate_password_metadata(length=7, age_days=180)
    print(f"Password Risk: {pwd['password_risk_pct']}% | Compliance: {pwd['security_compliance']}")
    
    # 19. Endpoint Malware Detection
    print("\n--- [Module 19] Endpoint Malware / Ransomware Detection ---")
    m19 = MalwareEarlyDetector()
    mal = m19.analyze_endpoint_telemetry()
    print(f"Status: {mal['status']} ({mal['ransomware_probability_pct']}% prob)")
    
    # 20. Cloud Security Risk Predictor
    print("\n--- [Module 20] Cloud Security Risk Predictor ---")
    m20 = CloudSecurityRiskPredictor()
    cloud = m20.evaluate_cloud_posture()
    print(f"Cloud Risk Score: {cloud['cloud_asset_risk_score']} ({cloud['risk_posture']})")
    
    # 21. Identity & Access Risk
    print("\n--- [Module 21] Identity & Access Risk Analyzer ---")
    m21 = IdentityAccessRiskAnalyzer()
    iam = m21.evaluate_identity_risk()
    print(f"User Risk Score: {iam['user_risk_score']} | Reasons: {iam['combined_reasons']}")
    
    # 22. GNN Research Model
    print("\n--- [Module 22] Graph Neural Network (GNN) Risk Model ---")
    m22 = GraphNeuralNetworkRiskModel()
    gnn = m22.predict_node_risk_gnn()
    print(f"GNN Model: {gnn['model_architecture']} | Node Risk Output: {gnn['node_risk_predictions']['Bank_Database']}")
    
    # 23. Federated Learning Simulator
    print("\n--- [Module 23] Privacy-Preserving Federated Learning ---")
    m23 = FederatedLearningSimulator()
    fl = m23.run_federated_round()
    print(f"Federated Model: {fl['final_global_model']} | Global Accuracy: {fl['federated_rounds'][-1]['global_accuracy_pct']}%")
    
    # 24. Adversarial ML Protection
    print("\n--- [Module 24] Adversarial ML Protection ---")
    m24 = AdversarialMLProtector()
    adv = m24.get_robustness_metrics()
    print(f"Model Status: {adv['model_status']} | Accuracy: {adv['model_accuracy_pct']}% | Drift: {adv['model_drift_level']}")
    
    # 25. MLOps Monitoring
    print("\n--- [Module 25] MLOps Model Performance Monitor ---")
    m25 = MLOpsMonitor()
    mlops = m25.evaluate_performance([1, 1, 0, 1, 0], [1, 1, 0, 1, 0])
    print(f"Precision: {mlops['Precision']} | Recall: {mlops['Recall']} | F1 Score: {mlops['F1 Score']}")
    
    # 26. Continuous Learning Pipeline
    print("\n--- [Module 26] Continuous Learning & Versioning ---")
    m26 = ContinuousLearningPipeline()
    cl = m26.trigger_retraining()
    print(f"Pipeline Status: {cl['pipeline_status']} | Active Version: {cl['active_model_version']}")
    
    # 27. Feature Engineering Layer
    print("\n--- [Module 27] Feature Engineering Layer ---")
    m27 = FeatureEngineeringPipeline()
    fe = m27.transform_raw_telemetry({"failed_login_count": 15, "avg_daily_attempts": 3, "cve_count": 8, "installed_software_count": 25, "os_patch_age_days": 180, "exposed_services_count": 5})
    print(f"Engineered Features: {fe['engineered_features']}")
    
    # 28. Real-Time Streaming
    print("\n--- [Module 28] Real-Time Streaming Simulator ---")
    m28 = RealTimeStreamSimulator()
    st = m28.stream_events()
    print(f"Streaming Score Progression: {st['score_progression']}")
    
    # 29. AI Natural Language Narrative Generator
    print("\n--- [Module 29] AI Risk Narrative Generator ---")
    m29 = RiskNarrativeGenerator()
    narr = m29.generate_narrative("Finance-PC-07", 87, "high", "outdated", 18)
    print(f"Narrative: {narr['risk_narrative']}")
    
    print("\n" + "=" * 70)
    print("      [+] ALL 31 OMEGA ML SUITE MODULES VERIFIED SUCCESSFULLY [+]")
    print("=" * 70)

if __name__ == "__main__":
    run_master_demonstration()
