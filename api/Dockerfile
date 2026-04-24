FROM python:3.9-slim

WORKDIR /app

# Install dependencies as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# SECURITY: Create 'devops' user
RUN useradd -m devops
USER devops

COPY . .

# Required Healthcheck (API uses port 8000)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

#FIXED: Using uvicorn to actually serve the API on port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
