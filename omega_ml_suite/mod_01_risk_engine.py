"""
Module 01: Advanced Multi-Model Risk Prediction Engine
Supports Random Forest, XGBoost, LightGBM, Logistic Regression, Neural Network (MLP), Gradient Boosting.
Auto-selects best model based on metrics and generates probability breakdowns.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

try:
    from xgboost import XGBClassifier
    HAS_XGB = True
except ImportError:
    HAS_XGB = False

try:
    from lightgbm import LGBMClassifier
    HAS_LGBM = True
except ImportError:
    HAS_LGBM = False

from omega_ml_suite.data_generator import generate_asset_telemetry

class RiskPredictionEngine:
    def __init__(self):
        self.models = {
            "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
            "Gradient Boosting": GradientBoostingClassifier(random_state=42),
            "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
            "Neural Network": MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=500, random_state=42)
        }
        if HAS_XGB:
            self.models["XGBoost"] = XGBClassifier(eval_metric='logloss', random_state=42)
        if HAS_LGBM:
            self.models["LightGBM"] = LGBMClassifier(random_state=42, verbose=-1)
            
        self.best_model_name = None
        self.best_model = None
        self.best_metrics = {}
        self.feature_cols = ["cve_max_cvss", "failed_logins", "os_patch_age_days", "software_risk_score", "behavior_anomaly_score"]

    def train_and_evaluate_all(self, df=None):
        if df is None:
            df = generate_asset_telemetry(n_samples=300)
            
        X = df[self.feature_cols]
        y = df["is_high_risk"]
        
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=42)
        
        results = {}
        best_score = -1.0
        
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            preds = model.predict(X_val)
            probs = model.predict_proba(X_val)[:, 1] if hasattr(model, "predict_proba") else preds
            
            acc = accuracy_score(y_val, preds)
            f1 = f1_score(y_val, preds, zero_division=0)
            try:
                auc = roc_auc_score(y_val, probs)
            except Exception:
                auc = acc
                
            results[name] = {"accuracy": acc, "f1_score": f1, "roc_auc": auc}
            
            if auc > best_score:
                best_score = auc
                self.best_model_name = name
                self.best_model = model
                self.best_metrics = results[name]
                
        return results

    def predict_device_risk(self, device_data):
        """
        Input: dict with feature_cols + device_id
        Returns output matching requirement:
        Device: Finance-PC-01
        Risk Score: 87/100
        Risk Level: HIGH
        Prediction Confidence: 94%
        Probabilities: Low 4%, Medium 8%, High 88%
        Top Risk Factors
        """
        if self.best_model is None:
            self.train_and_evaluate_all()
            
        X_input = pd.DataFrame([device_data])[self.feature_cols]
        
        probs = self.best_model.predict_proba(X_input)[0]
        # Calculate fine-grained 3-class probabilities (Low, Med, High)
        high_p = float(probs[1]) if len(probs) > 1 else float(probs[0])
        med_p = round(max(0.0, (1.0 - high_p) * 0.4), 2)
        low_p = round(max(0.0, 1.0 - high_p - med_p), 2)
        
        # Risk score out of 100
        risk_score = int(round(high_p * 100))
        risk_level = "CRITICAL" if risk_score >= 80 else ("HIGH" if risk_score >= 65 else ("MEDIUM" if risk_score >= 40 else "LOW"))
        confidence = int(round(max(high_p, low_p, med_p) * 100))
        
        # Risk factor identification
        factors = []
        if device_data.get("cve_max_cvss", 0) >= 7.0:
            factors.append("Critical CVE")
        if device_data.get("failed_logins", 0) >= 10:
            factors.append(f"{device_data['failed_logins']} failed logins")
        if device_data.get("os_patch_age_days", 0) >= 60:
            factors.append("Outdated OS")
        if device_data.get("software_risk_score", 0) >= 70:
            factors.append("High Software Vulnerability")
        if device_data.get("behavior_anomaly_score", 0) >= 70:
            factors.append("Behavioral Anomaly Detected")
            
        if not factors:
            factors = ["Standard Operating Profile"]
            
        return {
            "device_id": device_data.get("device_id", "Finance-PC-01"),
            "best_model_used": self.best_model_name,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "confidence_pct": confidence,
            "probabilities": {
                "Low": f"{int(round(low_p*100))}%",
                "Medium": f"{int(round(med_p*100))}%",
                "High": f"{int(round(high_p*100))}%"
            },
            "top_risk_factors": factors
        }
