"""
Module 09: Attack Graph & Risk Graph Engine
Generates topological risk graphs representing node vulnerability states and exposure chains.
"""

class RiskGraphEngine:
    def __init__(self):
        self.nodes = {
            "Internet": {"type": "External", "risk_score": 100, "status": "[RED] UNTRUSTED"},
            "Web Server": {"type": "DMZ", "risk_score": 78, "status": "[ORANGE] HIGH RISK"},
            "Application Server": {"type": "Internal", "risk_score": 62, "status": "[ORANGE] MEDIUM RISK"},
            "Database": {"type": "Secure Zone", "risk_score": 91, "status": "[RED] CRITICAL RISK"},
            "Backup Server": {"type": "Isolated", "risk_score": 24, "status": "[GREEN] LOW RISK"}
        }
        
        self.edges = [
            ("Internet", "Web Server"),
            ("Web Server", "Application Server"),
            ("Application Server", "Database"),
            ("Database", "Backup Server")
        ]

    def get_graph_topology(self):
        """Returns node risks and path risks for visual presentation."""
        critical_path_narrative = (
            "Compromise of Web Server could expose a direct lateral movement path toward the Database."
        )
        
        return {
            "nodes": self.nodes,
            "edges": self.edges,
            "critical_exposure_path": ["Internet", "Web Server", "Application Server", "Database"],
            "ai_narrative": critical_path_narrative
        }
