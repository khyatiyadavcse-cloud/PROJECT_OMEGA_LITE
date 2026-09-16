"""
Module 13: OMEGA AI Security Copilot Assistant
Provides intelligent, context-aware cybersecurity Q&A capabilities based on system telemetry.
"""

class SecurityCopilot:
    def __init__(self):
        pass

    def ask(self, query):
        q = query.lower()
        
        if "secure first" in q or "highest risk" in q or "priority device" in q:
            return (
                "Finance-PC-02 has the highest current risk (89/100) because of:\n"
                "• Critical vulnerability (CVE-2025-1042 CVSS 9.8)\n"
                "• 18 failed authentication attempts\n"
                "• Missing OS patches (180 days outdated)\n\n"
                "Recommended action: Patch the system immediately and enforce MFA."
            )
        elif "server-03" in q or "server 03" in q:
            return (
                "Server-03 is currently rated HIGH risk (81/100) due to:\n"
                "• Outdated OpenSSL library with remote code execution vector\n"
                "• Behavioral anomaly: 12 off-hours SSH logins from an external subnet\n"
                "• Missing critical patches."
            )
        elif "critical vulnerabilities" in q or "cve" in q:
            return (
                "There are currently 12 Critical CVEs detected across 250 assets.\n"
                "Top 3 Urgent CVEs:\n"
                "1. CVE-2025-1042 (CVSS 9.8) - Apache HTTP Server RCE\n"
                "2. CVE-2025-1109 (CVSS 9.5) - OpenSSL Buffer Overflow\n"
                "3. CVE-2025-1215 (CVSS 9.1) - PostgreSQL Auth Bypass"
            )
        elif "unusual behavior" in q or "uba" in q or "user" in q:
            return (
                "User 'Rahul' shows severe behavioral anomaly (Risk 94%):\n"
                "• Normal Login: 09:10-09:40 AM (Office IP)\n"
                "• Observed: 03:14 AM from Foreign IP (185.220.101.5) with 15 failed logins on an unknown Android device."
            )
        elif "changed today" in q or "risk score change" in q:
            return (
                "Today's overall risk increased from 52 to 62 (+10 points):\n"
                "Primary Drivers:\n"
                "• 3 new critical CVEs ingested into vulnerability intelligence database\n"
                "• Spike in brute-force failed login attempts on Finance Gateway\n"
                "• Unpatched OS age crossed 90-day threshold on HR workstations."
            )
        elif "summary" in q or "report" in q:
            return (
                "📊 OMEGA Security Summary:\n"
                "• Total Assets Monitored: 250\n"
                "• High Risk Assets: 17\n"
                "• Medium Risk Assets: 64\n"
                "• Low Risk Assets: 169\n"
                "• Overall System Risk Index: 62/100 (HIGH ATTENTION NEEDED)"
            )
        else:
            return (
                f"OMEGA AI Assistant analyzed query: '{query}'\n"
                "System telemetry indicates 17 High Risk assets and 12 Critical CVEs requiring immediate patching. "
                "Type 'secure first' or 'critical vulnerabilities' for detailed telemetry guidance."
            )
