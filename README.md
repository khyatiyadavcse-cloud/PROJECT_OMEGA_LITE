# PROJECT OMEGA LITE — Advanced Cyber Risk & AI/ML Security Engine

**PROJECT OMEGA LITE** is an enterprise-grade AI/ML cybersecurity intelligence suite that combines multi-model risk prediction, Explainable AI (SHAP), user behavior analytics (UBA), attack path graph simulations, MLOps, and real-time SOC command center monitoring.

---

## 🧠 Core AI/ML Modules (`omega_ml_suite`)

The system features 31 fully integrated Python AI/ML security modules:

1. **Multi-Model Risk Prediction Engine**: Compares Random Forest, XGBoost, LightGBM, Logistic Regression, Neural Network (MLP), and Gradient Boosting. Auto-selects the best model based on ROC-AUC / F1 score and outputs risk probabilities (Low/Med/High %).
2. **Dynamic Risk Score & Explainable Formula Layer**: Real-time score tracking over time with formula breakdown:
   $$\text{RiskScore} = w_1 V + w_2 L + w_3 P + w_4 S + w_5 B + w_6 A$$
3. **AI Vulnerability Intelligence**: Prioritizes 500+ CVEs down to Top 10 critical items using CVSS, exploitability, asset importance, internet exposure, patch status, and historical attack frequency.
4. **Unsupervised Anomaly Detection**: Isolation Forest, One-Class SVM, Autoencoder, and DBSCAN for detecting login time, IP location, and endpoint anomalies.
5. **User Behavior Analytics (UBA)**: Per-user baseline profile modeling (Rahul baseline) & behavioral risk elevation scoring.
6. **Account Takeover (ATO) Detection**: ATO compromise probability scoring with automated mitigation actions (Force Logout, Password Reset, Enforce MFA, Session Block).
7. **Network Anomaly Detection**: Bandwidth surge, port scan (e.g. 4444, 31337), packet rate, and protocol anomaly monitoring.
8. **Attack Path Prediction & Simulation**: Multi-hop lateral movement simulation (Asset A → Weak Password → Server B → Critical CVE → Database).
9. **Attack Graph / Risk Graph Engine**: Topological network risk graph (Internet → DMZ → App Server → Database) with color-coded risk nodes and exposure chain narratives.
10. **Explainable AI (XAI)**: SHAP-style waterfall feature attribution breakdown explaining top risk score contributors.
11. **Time-Series Risk Forecasting**: Temporal projection for future risk scores (+1 Day, +3 Days, +7 Days).
12. **Early Warning System**: Automatic threshold-cross alert trigger with multi-channel dispatchers (Email, Dashboard, Webhook, SMS/WhatsApp).
13. **OMEGA AI Security Copilot**: Interactive natural language cybersecurity assistant for context-aware Q&A on assets, CVEs, anomalies, and recommendations.
14. **Natural Language Security Reports**: Auto-generated executive security summary reports.
15. **What-If Risk Simulator**: Interactive risk reduction simulator for evaluating preventive controls (MFA, Patching, Password Strength).
16. **AI Recommendation Engine**: Prioritized security recommendations ordered by expected risk score reduction.
17. **Risk + Business Impact Engine**: Technical Risk × Business Asset Criticality composite scoring.
18. **Password Risk ML Analyzer**: Privacy-preserving password metadata risk evaluation (length, pattern, age, breach exposure).
19. **Endpoint Ransomware / Malware Detector**: Endpoint telemetry monitoring (CPU spikes, file modification rates, entropy changes, volume shadow copy deletion).
20. **Cloud Security Risk Predictor**: AWS/Azure/GCP cloud posture analysis (public S3 buckets, open 0.0.0.0/0 management ports, wildcard IAM policies).
21. **Identity & Access Risk (IAM)**: Privileged account, dormant account, and excessive RBAC permission risk scoring.
22. **Graph Neural Network (GNN) Model**: 2-Layer Graph Convolutional Network (GCN) for predicting cyber infrastructure graph node risks.
23. **Privacy-Preserving Federated Learning**: Multi-organization FedAvg collaborative model training without raw data transfer.
24. **Adversarial ML Protection**: Input bounds validation, data quality checks, and FGSM/PGD adversarial hardening monitoring.
25. **MLOps Model Performance Monitor**: Tracks Precision, Recall, F1 Score, ROC-AUC, FPR, FNR, and Population Stability Index (PSI) drift.
26. **Continuous Learning Pipeline**: Automated lifecycle (Data Ingestion → Validation → Feature Engineering → Retraining → Versioning: `OMEGA-v1` to `OMEGA-v3`).
27. **Feature Engineering Layer**: Domain feature transformations (failed login rate, vulnerability density, patch age factor, service exposure index).
28. **Real-Time Streaming Simulator**: Live event stream simulator pushing dynamic risk score updates.
29. **AI Natural Language Risk Narrative Engine**: Natural language explanation generator for asset risk profiles.
30. **SOC Command Center Dashboard**: Interactive Streamlit Web Command Center UI.
31. **Master Demo Runner & CLI**: Command line entry points (`python -m omega_ml_suite.cli`) and comprehensive unit test suite (`pytest`).

---

## 🚀 Quick Start Guide

### 1. Execute Master Demonstration
Run all 31 features sequentially in the terminal:
```bash
python omega_ml_suite/run_all_demo.py
# OR
python -m omega_ml_suite.cli run-all
```

### 2. Launch SOC Command Center Dashboard
Start the interactive web dashboard:
```bash
streamlit run omega_ml_suite/dashboard.py
```

### 3. Run Automated Unit Test Suite
Verify test coverage across all 31 modules:
```bash
pytest omega_ml_suite/tests/test_suite.py
```

---

## 📁 Repository Directory Structure

```
PROJECT_OMEGA_LITE/
├── Database/                              # Database SQL schema & dumps
├── Documentation/                         # Architectural & ER diagrams
├── README.md                              # Main documentation
└── omega_ml_suite/                        # AI/ML Security Engine
    ├── __init__.py
    ├── config.py                          # Risk weights & thresholds
    ├── data_generator.py                  # Synthetic telemetry dataset generator
    ├── mod_01_risk_engine.py              # Multi-model Risk Prediction Engine
    ├── mod_02_dynamic_risk.py             # Dynamic Risk Score & Explainable Formula
    ├── mod_03_vuln_intel.py               # AI Vulnerability Intelligence & CVE Top-10
    ├── mod_04_anomaly_detection.py        # Unsupervised Anomaly Detection
    ├── mod_05_uba.py                      # User Behavior Analytics (UBA)
    ├── mod_06_account_takeover.py         # Account Takeover (ATO) Detection
    ├── mod_07_network_anomaly.py          # Network Anomaly Detection
    ├── mod_08_attack_prediction.py        # Attack Path Simulation Engine
    ├── mod_09_attack_graph.py             # Risk Graph Topology Engine
    ├── mod_10_xai.py                      # Explainable AI (SHAP) Engine
    ├── mod_11_forecasting.py              # Time-Series Risk Forecasting
    ├── mod_12_early_warning.py            # Early Warning System
    ├── mod_13_copilot.py                  # OMEGA AI Security Copilot
    ├── mod_14_reports.py                  # Executive Report Generator
    ├── mod_15_what_if.py                  # What-If Risk Simulator
    ├── mod_16_recommendation.py           # Security Recommendation Engine
    ├── mod_17_business_impact.py          # Risk + Business Impact Engine
    ├── mod_18_password_risk.py            # Password Risk ML Analyzer
    ├── mod_19_malware_detection.py        # Endpoint Ransomware Detector
    ├── mod_20_cloud_security.py           # Cloud Security Risk Predictor
    ├── mod_21_identity_access.py          # IAM Risk Analyzer
    ├── mod_22_gnn_research.py             # Graph Neural Network Risk Model
    ├── mod_23_federated_learning.py       # Privacy-Preserving Federated Learning
    ├── mod_24_adversarial_ml.py           # Adversarial ML Protector
    ├── mod_25_mlops.py                    # MLOps Model Monitor
    ├── mod_26_continuous_learning.py      # Continuous Learning Pipeline
    ├── mod_27_feature_engineering.py      # Feature Engineering Layer
    ├── mod_28_realtime_streaming.py       # Real-Time Event Stream Simulator
    ├── mod_29_narrative_generator.py      # AI Risk Narrative Generator
    ├── dashboard.py                       # SOC Command Center Dashboard
    ├── cli.py                             # Unified CLI Runner
    ├── run_all_demo.py                    # Master End-to-End Demo Script
    └── tests/
        └── test_suite.py                  # Pytest Unit Test Suite
```
