"""
Module 04: Unsupervised Anomaly Detection Engine
Implements Isolation Forest, One-Class SVM, Autoencoder, and DBSCAN for detecting authentication & endpoint anomalies.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.cluster import DBSCAN
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

class AnomalyDetector:
    def __init__(self):
        self.iso_forest = IsolationForest(contamination=0.1, random_state=42)
        self.oc_svm = OneClassSVM(nu=0.1, kernel='rbf')
        self.dbscan = DBSCAN(eps=1.5, min_samples=3)
        self.autoencoder = MLPRegressor(hidden_layer_sizes=(4, 2, 4), max_iter=300, random_state=42)
        self.scaler = StandardScaler()
        self.is_fitted = False

    def fit_baseline(self, normal_data=None):
        """Fit baseline on normal operational behavior."""
        if normal_data is None:
            # Generate normal login telemetry (e.g. login hour 9-18, failed logins 0-2, IP distance low)
            np.random.seed(42)
            normal_data = pd.DataFrame({
                "login_hour": np.random.uniform(9, 18, 200),
                "failed_attempts": np.random.poisson(lam=0.5, size=200),
                "is_known_ip": np.ones(200),
                "is_known_device": np.ones(200)
            })
            
        scaled = self.scaler.fit_transform(normal_data)
        self.iso_forest.fit(scaled)
        self.oc_svm.fit(scaled)
        self.autoencoder.fit(scaled, scaled)
        self.dbscan.fit(scaled)
        self.is_fitted = True

    def detect_anomaly(self, sample_event):
        """
        Sample event format:
        {'login_hour': 3.28, 'failed_attempts': 15, 'is_known_ip': 0, 'is_known_device': 0}
        """
        if not self.is_fitted:
            self.fit_baseline()
            
        event_df = pd.DataFrame([sample_event])
        scaled_event = self.scaler.transform(event_df)
        
        # 1. Isolation Forest score
        iso_pred = self.iso_forest.predict(scaled_event)[0] # -1 anomaly, 1 normal
        iso_score = -self.iso_forest.score_samples(scaled_event)[0]
        
        # 2. One-Class SVM
        svm_pred = self.oc_svm.predict(scaled_event)[0]
        
        # 3. Autoencoder Reconstruction Error
        reconstructed = self.autoencoder.predict(scaled_event)
        recon_error = float(np.mean((scaled_event - reconstructed) ** 2))
        
        # Combined Anomaly Score 0..100
        combined_score = min(100, int(round((iso_score * 50 + recon_error * 40 + (1 if iso_pred==-1 else 0)*20))))
        is_anomalous = combined_score >= 60
        
        return {
            "status": "[!] ANOMALY DETECTED" if is_anomalous else "NORMAL",
            "anomaly_score_pct": combined_score,
            "models_flagged": {
                "Isolation Forest": "ANOMALY" if iso_pred == -1 else "NORMAL",
                "One-Class SVM": "ANOMALY" if svm_pred == -1 else "NORMAL",
                "Autoencoder Error": round(recon_error, 4)
            },
            "event_summary": sample_event
        }
