"""
Module 32: OMEGA REST API Server
Provides lightweight JSON REST API endpoints for risk prediction, CVE intel, What-If simulation, and Copilot.
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from omega_ml_suite.mod_01_risk_engine import RiskPredictionEngine
from omega_ml_suite.mod_03_vuln_intel import VulnerabilityIntelligenceEngine
from omega_ml_suite.mod_13_copilot import SecurityCopilot
from omega_ml_suite.mod_15_what_if import WhatIfRiskSimulator

class OMEGARequestHandler(BaseHTTPRequestHandler):
    risk_engine = RiskPredictionEngine()
    vuln_engine = VulnerabilityIntelligenceEngine()
    copilot = SecurityCopilot()
    whatif = WhatIfRiskSimulator()

    def do_GET(self):
        if self.path == "/api/status":
            self._send_json({"status": "ONLINE", "service": "OMEGA AI Security API v2.0"})
        elif self.path == "/api/cve_top10":
            data = self.vuln_engine.prioritize_vulnerabilities(top_n=10)
            self._send_json(data)
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len) if content_len > 0 else b"{}"
        try:
            req_data = json.loads(body.decode('utf-8'))
        except Exception:
            req_data = {}

        if self.path == "/api/predict":
            res = self.risk_engine.predict_device_risk(req_data)
            self._send_json(res)
        elif self.path == "/api/copilot":
            query = req_data.get("query", "Which device should I secure first?")
            ans = self.copilot.ask(query)
            self._send_json({"query": query, "answer": ans})
        elif self.path == "/api/whatif":
            initial = req_data.get("initial_risk", 91)
            res = self.whatif.simulate_controls(initial_risk=initial)
            self._send_json(res)
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

def start_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, OMEGARequestHandler)
    print(f"[+] OMEGA REST API Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    start_server(8080)
