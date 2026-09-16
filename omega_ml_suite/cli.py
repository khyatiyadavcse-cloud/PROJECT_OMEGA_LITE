"""
CLI Entry Point for OMEGA ML Suite.
Command-line interface to execute ML predictions, run simulations, launch dashboard, or execute tests.
"""

import sys
import argparse
from omega_ml_suite.run_all_demo import run_master_demonstration

def main():
    parser = argparse.ArgumentParser(description="OMEGA AI Security & ML Suite CLI Runner")
    parser.add_argument("command", nargs="?", default="run-all", choices=["run-all", "dashboard", "test"],
                        help="Command to run: 'run-all' (master demo), 'dashboard' (launch Streamlit UI), 'test' (run pytest suite)")
    
    args = parser.parse_args()
    
    if args.command == "run-all":
        print("Executing OMEGA ML Suite Master Demonstration...\n")
        run_master_demonstration()
    elif args.command == "dashboard":
        import subprocess
        print("Launching OMEGA SOC Command Center Dashboard...")
        subprocess.run(["streamlit", "run", "omega_ml_suite/dashboard.py"])
    elif args.command == "test":
        import pytest
        print("Running OMEGA ML Suite Unit Test Suite...")
        sys.exit(pytest.main(["-v", "omega_ml_suite/tests/test_suite.py"]))

if __name__ == "__main__":
    main()
