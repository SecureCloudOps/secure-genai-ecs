# DevSecOps: Secure GenAI API on AWS ECS 🚀🔐
<p align="left">

  <!-- Core Technologies -->
  <img src="https://img.shields.io/badge/AWS-ECS%20Fargate-success?style=flat-square&logo=amazonaws" />
  <img src="https://img.shields.io/badge/API-GenAI-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Infrastructure-Terraform-purple?style=flat-square&logo=terraform" />
  <img src="https://img.shields.io/badge/Container-Docker-informational?style=flat-square&logo=docker" />

  <!-- Security Focus -->
  <img src="https://img.shields.io/badge/Security-Shift--Left-success?style=flat-square" />
  <img src="https://img.shields.io/badge/IaC%20Scan-tfsec-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Compliance-Checkov-success?style=flat-square" />
  <img src="https://img.shields.io/badge/Runtime-WAF-informational?style=flat-square" />

  <!-- CI/CD -->
  <img src="https://img.shields.io/badge/Pipeline-GitHub%20Actions-success?style=flat-square&logo=githubactions" />
  <img src="https://img.shields.io/badge/Build-Automated-blue?style=flat-square" />

</p>


**Author**: Mohamed A. Mohamed 



## Project Directory Structure

```plaintext

├── api/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── terraform/
│   ├── main.tf
│   ├── provider.tf
│   └── variables.tf
└── README.md
```

## 📐 Architecture Diagram


![image](https://imgur.com/TGX5zKZ.png)

---



A hands‑on DevSecOps portfolio project showcasing:



* **Secure IaC**: Fully modular Terraform for AWS networking, IAM, ECS/Fargate, ALB, WAF, CloudTrail.
* **Shift‑Left Security**: Policy‑as‑code gates (Trivy, tfsec, Checkov) in CI to catch misconfigurations before deployment.
* **Automated CI/CD**: GitHub Actions builds, scans, pushes Docker images, and triggers Terraform deployments—end‑to‑end pipeline.
* **Compliance & Monitoring**: CloudTrail logs in encrypted S3, AWS WAFv2,  GuardDuty, CloudWatch dashboards for observability.


---
## Why This Project Matters

In an era where rapid innovation often outpaces security, this Secure GenAI API Deployment project demonstrates how to build and run cutting-edge containerized AI services without sacrificing safety or compliance. By integrating hardened Docker images, least-privilege IAM roles, encrypted secrets, and real-time monitoring (CloudTrail & GuardDuty) from Day One, it not only showcases best practices in DevSecOps today but lays the groundwork for tomorrow’s AI-driven infrastructures. 

---

## 🔍 Security Posture & Compliance

| Layer                  | Controls & Tools                                   |
| ---------------------- | -------------------------------------------------- |
| **Network**            | VPC with private tasks subnets, public ALB, NAT GW |
| **Authentication**     | IAM least‑privilege roles scoped to ECR + Secrets  |
| **Secrets Management** | OpenAI key in AWS Secrets Manager with rotation    |
| **Infrastructure**     | Terraform modules, tfsec/Checkov policies          |
| **Container Security** | Distroless base image, ECR image scanning on push  |
| **Edge Protection**    | AWS WAFv2 Managed Rules (SQLi, XSS, bots)          |
| **Audit & Monitoring** | CloudTrail → encrypted S3 + CloudWatch, GuardDuty  |
---

![image](https://imgur.com/aUDvO9g.png)
![image](https://imgur.com/ZwhZByu.png)
![image](https://imgur.com/hNkWlnO.png)
![image](https://imgur.com/NVRVD5N.png)


## ⚙️ CI/CD Pipeline & Security Gates

1. **Checkout & AWS Auth**
2. **Docker Build** & **Trivy scan**
3. **Terraform fmt & validate**
4. **tfsec** & **Checkov** compliance scans
5. **ECR Push** 
6. **Terraform Init & Apply**

All secrets and credentials are kept in GitHub Secrets. No hard‑coded values.

---
## Conclusion

This project underscores the critical intersection of innovation and security in today's cloud-native environments. By containerizing a GenAI API on AWS ECS Fargate, enforcing hardened Docker images, applying least-privilege IAM roles, and automating infrastructure with Terraform, you’ve built not just a functional service but a replicable security blueprint.

---
