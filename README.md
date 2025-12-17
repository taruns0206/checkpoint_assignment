# checkpoint_assignment
Repo created for checkpoint assignment
# DevOps Home Assignment

## Overview
This project demonstrates Infrastructure as Code and CI/CD best practices by:
- Provisioning AWS infrastructure using Terraform & Terragrunt
- Deploying a private S3 bucket accessed only via CloudFront
- Processing and uploading data using Python
- Automating deployment using GitHub Actions

---

## Architecture
- **S3**: Private bucket for JSON storage
- **CloudFront**: Secure access to S3 using Origin Access Control
- **Terraform + Terragrunt**: Modular IaC
- **GitHub Actions**: CI/CD pipeline
- **Python**: Data processing and validation

---

## Terraform & Terragrunt
Resources created:
- S3 bucket (private)
- CloudFront distribution
- Origin Access Control
- Secure bucket policy

All resources include required tags:
- Name
- Owner
- Terraform

---

## Python Logic
1. Download products JSON from dummyjson.com
2. Filter products with price >= 100
3. Save results to a new JSON file
4. Upload file to S3
5. Download file via CloudFront
6. Validate downloaded file is valid JSON

---

## CI/CD Pipeline
The GitHub Actions workflow has **two distinct steps**:
1. Deploy infrastructure (Terraform + Terragrunt)
2. Run Python application

Secrets are handled securely via GitHub Secrets.

---

## Security Considerations
- No AWS credentials stored in code
- S3 access restricted to CloudFront only
- GitHub Secrets used for credentials

---

## How to Run Locally
```bash
pip install -r app/requirements.txt
python app/process_products.py
