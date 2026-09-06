# 🚀 DevOps Production Pipeline

A production-grade CI/CD pipeline using GitHub Actions, Docker, and Kubernetes with strong focus on automation, security, and multi-environment deployments.

---

## 📌 What This Project Does

This project simulates a real-world DevOps pipeline where:

- Code is validated before merging
- Security is enforced at multiple levels
- Docker images are built and scanned
- Images are pushed to GHCR
- Deployments happen safely across environments

---

## ⚙️ Tech Stack

- CI/CD → GitHub Actions
- Containers → Docker
- Registry → GHCR
- Orchestration → Kubernetes
- Language → Python

### 🔐 Security Tools
- Flake8 → Code quality
- Bandit → Code security
- Safety → Dependency scan
- Trivy → Docker image scan

---

## 🔄 Pipeline Flow

Developer → PR → CI → Merge → Build → Scan → Push → Deploy

---

## 🧪 PR Checks

- Lint check (flake8)
- Security scan (bandit)
- Dependency scan (safety)
- Unit tests (pytest)
- Docker build test

---

## 📦 Main Pipeline

- Build Docker image
- Scan image (Trivy)
- Push to GHCR
- Deploy to staging

---

## 🌍 Environments

- Dev
- QA
- Staging
- Production

Same image is used across all environments, only configs change.

---

## 🔐 Security

- Protected main branch
- Required PR approvals
- Required status checks
- Code scanning
- Dependency scanning
- Container scanning
- Environment secrets

---

## 📁 Project Structure

.
├── .github/workflows/
├── Dockerfile
├── main.py
├── requirements.txt
└── tests/

---

## 🚀 Future Scope

- Multi-cluster deployment
- Monitoring (Prometheus, Grafana)
- Logging (ELK)
- Blue/Green deployments

---

## 👨‍💻 Author

Kshithi

