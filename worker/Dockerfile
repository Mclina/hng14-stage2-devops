FROM python:3.9-slim

WORKDIR /app

# Install requirements as root first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create and switch to non-root user
RUN useradd -m devops
USER devops

COPY . .

# Since worker doesn't have a port, we check if the process is alive
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD pgrep python || exit 1

CMD ["python", "worker.py"]
