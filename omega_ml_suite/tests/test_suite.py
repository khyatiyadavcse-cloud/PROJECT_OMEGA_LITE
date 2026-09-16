"""
Unit Test Suite for OMEGA ML Suite.
Tests all 31 security modules to ensure robustness and correctness.
"""

import pytest
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

def test_01_risk_engine():
    engine = RiskPredictionEngine()
    res = engine.predict_device_risk({
        "device_id": "Test-PC",
        "cve_max_cvss": 9.0,
        "failed_logins": 15,
        "os_patch_age_days": 100,
        "software_risk_score": 75,
        "behavior_anomaly_score": 80
    })
    assert "risk_score" in res
    assert res["risk_score"] > 0
    assert "top_risk_factors" in res

def test_02_dynamic_risk():
    m = DynamicRiskEngine()
    res = m.calculate_explainable_score(90, 80, 70, 60, 50, 40)
    assert res["formula_score"] > 0
    assert "breakdown" in res

def test_03_vuln_intel():
    v = VulnerabilityIntelligenceEngine()
    res = v.prioritize_vulnerabilities(top_n=5)
    assert len(res["top_vulnerabilities"]) == 5

def test_04_anomaly_detection():
    ad = AnomalyDetector()
    res = ad.detect_anomaly({"login_hour": 3.0, "failed_attempts": 10, "is_known_ip": 0, "is_known_device": 0})
    assert res["status"] in ["⚠️ ANOMALY DETECTED", "NORMAL"]

def test_05_uba():
    uba = UserBehaviorAnalytics()
    res = uba.analyze_user_event("Rahul")
    assert res["behavioral_risk_score"] > 0

def test_06_account_takeover():
    ato = AccountTakeoverDetector()
    res = ato.evaluate_account({"today_logins": 40, "failed_attempts": 10, "is_new_ip": True, "is_new_device": True})
    assert res["ato_probability_pct"] >= 50

def test_07_network_anomaly():
    net = NetworkAnomalyDetector()
    res = net.analyze_network_stream({"bandwidth_mb_min": 500, "active_ports": [4444]})
    assert res["network_anomaly_score_pct"] > 0

def test_08_attack_prediction():
    att = AttackPathSimulator()
    res = att.simulate_attack_path()
    assert len(res["simulated_hops"]) == 3

def test_09_attack_graph():
    rg = RiskGraphEngine()
    res = rg.get_graph_topology()
    assert "Database" in res["nodes"]

def test_10_xai():
    xai = ExplainableAIEngine()
    res = xai.explain_prediction()
    assert len(res["top_contributors"]) > 0

def test_11_forecasting():
    fc = RiskForecaster()
    res = fc.forecast_risk(60)
    assert len(res["forecast"]) == 4

def test_12_early_warning():
    ew = EarlyWarningSystem()
    res = ew.evaluate_risk_delta("Server-02", 50, 85)
    assert res["alert_triggered"] is True

def test_13_copilot():
    cp = SecurityCopilot()
    ans = cp.ask("Which device should I secure first?")
    assert "Finance-PC-02" in ans

def test_14_reports():
    rep = NaturalLanguageReportGenerator()
    res = rep.generate_weekly_report()
    assert "WEEKLY SECURITY EXECUTIVE SUMMARY" in res["report_text"]

def test_15_what_if():
    sim = WhatIfRiskSimulator()
    res = sim.simulate_controls(90, True, True, True)
    assert res["predicted_risk_score"] < 90

def test_16_recommendation():
    re = SecurityRecommendationEngine()
    res = re.get_recommendations(85)
    assert len(res["prioritized_actions"]) > 0

def test_17_business_impact():
    bi = BusinessImpactEngine()
    res = bi.calculate_business_risk("Bank Database", 65, "Bank Database")
    assert res["composite_business_risk_score"] > 65

def test_18_password_risk():
    pwd = PasswordRiskAnalyzer()
    res = pwd.evaluate_password_metadata(length=6)
    assert res["password_risk_pct"] > 0

def test_19_malware_detection():
    mal = MalwareEarlyDetector()
    res = mal.analyze_endpoint_telemetry()
    assert res["ransomware_probability_pct"] > 0

def test_20_cloud_security():
    cloud = CloudSecurityRiskPredictor()
    res = cloud.evaluate_cloud_posture()
    assert res["cloud_asset_risk_score"] > 0

def test_21_identity_access():
    iam = IdentityAccessRiskAnalyzer()
    res = iam.evaluate_identity_risk()
    assert res["user_risk_score"] > 0

def test_22_gnn_research():
    gnn = GraphNeuralNetworkRiskModel()
    res = gnn.predict_node_risk_gnn()
    assert "node_risk_predictions" in res

def test_23_federated_learning():
    fl = FederatedLearningSimulator()
    res = fl.run_federated_round()
    assert len(res["federated_rounds"]) == 3

def test_24_adversarial_ml():
    adv = AdversarialMLProtector()
    res = adv.get_robustness_metrics()
    assert res["model_accuracy_pct"] > 90

def test_25_mlops():
    m = MLOpsMonitor()
    res = m.evaluate_performance([1, 0, 1], [1, 0, 1])
    assert res["Precision"] == "100%"

def test_26_continuous_learning():
    cl = ContinuousLearningPipeline()
    res = cl.trigger_retraining()
    assert res["active_model_version"] == "OMEGA-v3.0"

def test_27_feature_engineering():
    fe = FeatureEngineeringPipeline()
    res = fe.transform_raw_telemetry({"failed_login_count": 10, "avg_daily_attempts": 2})
    assert res["engineered_features"]["failed_login_rate"] == 5.0

def test_28_realtime_streaming():
    st = RealTimeStreamSimulator()
    res = st.stream_events()
    assert len(res["score_progression"]) == 4

def test_29_narrative_generator():
    ng = RiskNarrativeGenerator()
    res = ng.generate_narrative("Finance-PC-07", 87, "high", "outdated", 18)
    assert "Finance-PC-07 is currently classified as HIGH RISK" in res["risk_narrative"]

def test_30_db_connector():
    from omega_ml_suite.db_connector import DatabaseConnector
    db = DatabaseConnector()
    res = db.export_ml_scores_to_sql()
    assert res["status"] == "SQL EXPORT SUCCESSFUL"
    assert res["records_exported"] == 50

