"""
Module 20: Cloud Security Risk Predictor
Analyzes AWS/Azure/GCP cloud configuration metadata for misconfigurations and posture risks.
"""

class CloudSecurityRiskPredictor:
    def __init__(self):
        pass

    def evaluate_cloud_posture(self, provider="AWS", cloud_metadata=None):
        """
        Input metadata format:
        {
          "public_s3_buckets": 3,
          "open_management_ports": ["0.0.0.0/0:22", "0.0.0.0/0:3389"],
          "wildcard_iam_policies": 5,
          "missing_at_rest_encryption": True
        }
        """
        if cloud_metadata is None:
            cloud_metadata = {
                "public_s3_buckets": 3,
                "open_management_ports": ["0.0.0.0/0:22", "0.0.0.0/0:3389"],
                "wildcard_iam_policies": 5,
                "missing_at_rest_encryption": True
            }
            
        score = 0
        findings = []
        
        buckets = cloud_metadata.get("public_s3_buckets", 0)
        if buckets > 0:
            score += 30
            findings.append(f"{buckets} public storage buckets exposed to internet")
            
        ports = cloud_metadata.get("open_management_ports", [])
        if ports:
            score += 25
            findings.append(f"Management ports open to 0.0.0.0/0: {ports}")
            
        iam = cloud_metadata.get("wildcard_iam_policies", 0)
        if iam > 0:
            score += 20
            findings.append(f"{iam} overly permissive wildcard (AdministratorAccess) IAM policies")
            
        if cloud_metadata.get("missing_at_rest_encryption", False):
            score += 15
            findings.append("KMS/AES-256 encryption disabled on data volumes")
            
        cloud_risk = min(100, score)
        
        return {
            "cloud_provider": provider,
            "cloud_asset_risk_score": cloud_risk,
            "risk_posture": "CRITICAL MISCONFIGURATION" if cloud_risk >= 75 else "SECURE",
            "findings": findings
        }
