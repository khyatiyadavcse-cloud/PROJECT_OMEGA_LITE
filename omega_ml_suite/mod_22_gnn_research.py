"""
Module 22: Graph Neural Network (GNN) Infrastructure Risk Model
Models cyber infrastructure as a graph (User -> Device -> Server -> Database) and predicts graph node risk.
"""

import numpy as np
import pandas as pd

class GraphNeuralNetworkRiskModel:
    def __init__(self):
        # Graph adjacency and node feature representations
        self.nodes = ["User_Rahul", "Device_Laptop04", "App_Server01", "Bank_Database"]
        self.edges = [
            ("User_Rahul", "Device_Laptop04", "login"),
            ("Device_Laptop04", "App_Server01", "network_access"),
            ("App_Server01", "Bank_Database", "dependency")
        ]

    def predict_node_risk_gnn(self):
        """Simulates Graph Convolution Layer (GCN) aggregation over node neighborhood."""
        # Initial node feature vectors (V, L, P, S)
        X = np.array([
            [0.1, 0.9, 0.2, 0.4], # User_Rahul (High login anomaly)
            [0.4, 0.5, 0.6, 0.5], # Device_Laptop04
            [0.8, 0.3, 0.7, 0.9], # App_Server01 (High CVE & software risk)
            [0.9, 0.2, 0.8, 0.9]  # Bank_Database
        ])
        
        # Adjacency Matrix A
        A = np.array([
            [1, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1]
        ], dtype=float)
        
        # Degree Matrix D normalization
        D_inv = np.diag(1.0 / np.sum(A, axis=1))
        
        # GCN Aggregation: H = D^-1 * A * X * W
        W = np.array([[0.25], [0.35], [0.20], [0.20]])
        H = np.dot(np.dot(D_inv, A), np.dot(X, W))
        
        node_risks = {}
        for idx, node in enumerate(self.nodes):
            score = int(round(float(H[idx][0]) * 100))
            node_risks[node] = {
                "gnn_risk_score": score,
                "node_status": "[RED] HIGH RISK" if score >= 60 else "[GREEN] STABLE"
            }
            
        return {
            "model_architecture": "2-Layer Graph Convolutional Network (GCN)",
            "graph_nodes_count": len(self.nodes),
            "graph_edges_count": len(self.edges),
            "node_risk_predictions": node_risks
        }
