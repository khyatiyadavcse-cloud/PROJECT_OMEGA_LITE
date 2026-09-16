"""
CLI Entry Point for OMEGA ML Suite.
Command-line interface to execute ML predictions, run simulations, launch dashboard, or execute tests.
"""

import sys
import argparse
from omega_ml_suite.run_all_demo import run_master_demonstration

def main():
    parser = argparse.ArgumentParser(description="OMEGA AI Security & ML Suite CLI Runner")
    parser.add_argument("command", nargs="?", default="run-all", choices=["run-all", "dashboard", "dashboard-html", "api", "export-sql", "test"],
                        help="Command to run: 'run-all' (master demo), 'dashboard' (Streamlit UI), 'dashboard-html' (open HTML UI), 'api' (start REST server), 'export-sql' (generate DB seed), 'test' (run test suite)")
    
    args = parser.parse_args()
    
    if args.command == "run-all":
        print("Executing OMEGA ML Suite Master Demonstration...\n")
        run_master_demonstration()
    elif args.command == "dashboard":
        import subprocess
        print("Launching OMEGA SOC Command Center Dashboard (Streamlit)...")
        subprocess.run(["streamlit", "run", "omega_ml_suite/dashboard.py"])
    elif args.command == "dashboard-html":
        import webbrowser
        import os
        html_path = os.path.abspath("omega_ml_suite/dashboard.html")
        print(f"Opening Standalone HTML SOC Dashboard: {html_path}")
        webbrowser.open(f"file://{html_path}")
    elif args.command == "api":
        from omega_ml_suite.api_server import start_server
        start_server(8080)
    elif args.command == "export-sql":
        from omega_ml_suite.db_connector import DatabaseConnector
        db = DatabaseConnector()
        res = db.export_ml_scores_to_sql()
        print(f"[+] SQL Export Result: {res}")
    elif args.command == "test":
        import pytest
        print("Running OMEGA ML Suite Unit Test Suite...")
        sys.exit(pytest.main(["-v", "omega_ml_suite/tests/test_suite.py"]))

if __name__ == "__main__":
    main()
