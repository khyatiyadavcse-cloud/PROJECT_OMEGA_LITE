"""
Module 30: OMEGA SOC Command Center Interactive Dashboard
Built with Streamlit for real-time visualization of all 31 AI/ML security suite features.
"""

import streamlit as st
import pandas as pd
import numpy as np

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

def main():
    st.set_page_config(page_title="OMEGA SOC Command Center", layout="wide", page_icon="🛡️")
    
    st.title("🛡️ OMEGA SECURITY COMMAND CENTER")
    st.caption("AI/ML Cyber Risk Prediction, Anomaly Detection & SOC Intelligence Suite")
    
    # Header Metric Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Assets", "250", "Active Monitored")
    col2.metric("High Risk Assets", "17", "+2 today", delta_color="inverse")
    col3.metric("Medium Risk", "64", "-1 today")
    col4.metric("Low Risk", "169", "Stable")
    col5.metric("Overall Risk Score", "62 / 100", "↗ High Attention", delta_color="inverse")
    
    st.divider()
    
    tabs = st.tabs([
        "🧠 Risk Prediction & XAI",
        "🔍 Vuln Intelligence",
        "🤖 Anomaly & UBA",
        "🧩 Attack Graph & Simulator",
        "🔄 What-If & Recommendations",
        "📈 Forecasting & Streaming",
        "🧠 AI Security Copilot",
        "📝 Reports & MLOps"
    ])
    
    # TAB 1: Risk Prediction & XAI
    with tabs[0]:
        st.subheader("1. Multi-Model Risk Prediction & Explainable AI (SHAP)")
        engine = RiskPredictionEngine()
        res = engine.predict_device_risk({
            "device_id": "Finance-PC-01",
            "cve_max_cvss": 9.8,
            "failed_logins": 18,
            "os_patch_age_days": 180,
            "software_risk_score": 88,
            "behavior_anomaly_score": 92
        })
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**Device:** `{res['device_id']}`")
            st.markdown(f"**Risk Score:** `{res['risk_score']} / 100` ({res['risk_level']})")
            st.markdown(f"**Prediction Confidence:** `{res['confidence_pct']}%`")
            st.markdown(f"**Best Model Selected:** `{res['best_model_used']}`")
            st.json(res["probabilities"])
            
        with c2:
            st.markdown("**Top Risk Factors:**")
            for f in res["top_risk_factors"]:
                st.write(f"- {f}")
                
            xai_eng = ExplainableAIEngine()
            exp = xai_eng.explain_prediction(device_id="Finance-PC-01", risk_score=res["risk_score"])
            st.markdown("**Explainable AI (SHAP Breakdown):**")
            st.dataframe(pd.DataFrame(exp["top_contributors"]))
            
    # TAB 2: Vuln Intelligence
    with tabs[1]:
        st.subheader("3. AI Vulnerability Intelligence (500 CVEs -> Top 10 Priority)")
        v_engine = VulnerabilityIntelligenceEngine()
        cve_results = v_engine.prioritize_vulnerabilities()
        st.dataframe(pd.DataFrame(cve_results["top_vulnerabilities"]))
        
    # TAB 3: Anomaly & UBA
    with tabs[2]:
        st.subheader("4 & 5. Anomaly Detection & User Behavior Analytics (UBA)")
        u1, u2 = st.columns(2)
        with u1:
            st.markdown("#### Unsupervised Anomaly Detector")
            ad = AnomalyDetector()
            out = ad.detect_anomaly({"login_hour": 3.28, "failed_attempts": 15, "is_known_ip": 0, "is_known_device": 0})
            st.write(out["status"])
            st.write(f"Anomaly Score: {out['anomaly_score_pct']}%")
            st.json(out["models_flagged"])
            
        with u2:
            st.markdown("#### User Behavior Analytics (UBA)")
            uba = UserBehaviorAnalytics()
            uba_out = uba.analyze_user_event("Rahul")
            st.write(f"User: **{uba_out['user']}**")
            st.write(f"Behavioral Risk Score: **{uba_out['behavioral_risk_score']}** ({uba_out['behavioral_risk_trend']})")
            st.write("Deviations:", uba_out["detected_deviations"])

    # TAB 4: Attack Graph & Simulator
    with tabs[3]:
        st.subheader("8 & 9. Attack Path Simulation & Topological Risk Graph")
        sim = AttackPathSimulator()
        path = sim.simulate_attack_path()
        st.write(f"**Potential Attack Path Risk:** `{path['overall_attack_path_risk']}` ({path['path_compromise_probability_pct']}% compromise probability)")
        st.table(pd.DataFrame(path["simulated_hops"]))
        
        rg = RiskGraphEngine()
        graph = rg.get_graph_topology()
        st.write("**Topological Node Risks:**")
        st.json(graph["nodes"])

    # TAB 5: What-If & Recommendations
    with tabs[4]:
        st.subheader("15 & 16. What-If Risk Simulator & AI Recommendation Engine")
        w1, w2 = st.columns(2)
        with w1:
            st.markdown("#### Interactive What-If Simulator")
            mfa = st.checkbox("Enable MFA", value=True)
            patch = st.checkbox("Install OS Patch", value=True)
            pwd = st.checkbox("Strong Password Policy", value=True)
            
            wis = WhatIfRiskSimulator()
            sim_res = wis.simulate_controls(initial_risk=91, apply_mfa=mfa, apply_patch=patch, apply_strong_password=pwd)
            st.metric("Predicted Risk", f"{sim_res['predicted_risk_score']}", f"-{sim_res['total_risk_reduction']} pts", delta_color="normal")
            
        with w2:
            st.markdown("#### Prioritized AI Recommendations")
            re = SecurityRecommendationEngine()
            recs = re.get_recommendations(89)
            st.dataframe(pd.DataFrame(recs["remediation_roadmap"]))

    # TAB 6: Forecasting & Streaming
    with tabs[5]:
        st.subheader("11 & 28. Time-Series Risk Forecasting & Real-Time Event Stream")
        f_col, s_col = st.columns(2)
        with f_col:
            st.markdown("#### Time-Series Risk Forecast")
            forecaster = RiskForecaster()
            f_res = forecaster.forecast_risk(61)
            st.dataframe(pd.DataFrame(f_res["forecast"]))
            
        with s_col:
            st.markdown("#### Real-Time Event Streaming")
            streamer = RealTimeStreamSimulator()
            st_res = streamer.stream_events()
            st.line_chart(pd.DataFrame(st_res["stream_ticks"]).set_index("time")["score"])

    # TAB 7: AI Security Copilot
    with tabs[6]:
        st.subheader("13. OMEGA AI Security Copilot Assistant")
        copilot = SecurityCopilot()
        user_q = st.text_input("Ask OMEGA AI Copilot:", value="Which device should I secure first?")
        if user_q:
            answer = copilot.ask(user_q)
            st.info(f"**AI Assistant:**\n\n{answer}")

    # TAB 8: Reports & MLOps
    with tabs[7]:
        st.subheader("14 & 25. Executive Reports & MLOps Model Monitoring")
        rep_gen = NaturalLanguageReportGenerator()
        rep = rep_gen.generate_weekly_report()
        st.code(rep["report_text"])
        
        st.markdown("#### MLOps Model Monitoring")
        adv = AdversarialMLProtector()
        st.json(adv.get_robustness_metrics())

if __name__ == "__main__":
    main()
