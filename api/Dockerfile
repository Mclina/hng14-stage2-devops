# Stage 1: Build stage
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Final stage
FROM python:3.9-slim
WORKDIR /app

# Create a non-root user for security (Stage 2 Requirement)
RUN useradd -m devops
USER devops

# Copy only the necessary files from the builder
COPY --from=builder /root/.local /home/devops/.local
COPY . .

# Set path to include the local bin
ENV PATH=/home/devops/.local/bin:$PATH

# Add a Healthcheck (Stage 2 Requirement)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
