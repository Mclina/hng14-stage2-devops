# hng14-stage2-devops
# HNG Stage 2 - DevOps Job Processor

This repository contains a containerized microservices application consisting of a FastAPI API, a Python Worker, and a Redis database. This project was developed as part of the HNG Stage 2 DevOps track to demonstrate proficiency in container orchestration, security, and CI/CD.

## 🚀 Features
- **FastAPI Core:** High-performance API for job submission and status tracking.
- **Background Processing:** Python-based worker for asynchronous task handling.
- **Infrastructure:** Fully orchestrated using Docker Compose.
- **Security:** Services run as non-root users (`devops`) to ensure the principle of least privilege.
- **Health Monitoring:** Automated health checks for service synchronization and reliability.

---

## 🛠️ Tech Stack
- **Languages:** Python 3.9
- **Frameworks:** FastAPI
- **Storage:** Redis (Alpine-based)
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions

---

## 🚦 Getting Started

### Prerequisites
- Docker and Docker Compose installed.
- Git (for cloning the repository).

### Installation & Deployment
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd hng14-stage2-devops
Spin up the containers:

Bash
docker compose up --build -d
Verify the services:
You can check if the API is running by using curl:

Bash
curl http://localhost:8000/health
📂 Project Structure
/api: The FastAPI application code and Dockerfile.

/worker: The background worker logic and Dockerfile.

docker-compose.yml: Orchestration file for all services.

FIXES.md: Detailed log of bug fixes and infrastructure improvements.

🛡️ Security & Optimization
Multi-stage builds: Optimized Docker images to reduce attack surface and build size.

Non-root execution: All processes are restricted to the devops user.

Resource Limits: CPU and Memory caps are enforced via Docker Compose to prevent resource exhaustion.
