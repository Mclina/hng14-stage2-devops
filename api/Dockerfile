# Stage 1: Build dependencies (The 'builder' stage)
FROM python:3.9-slim as builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final Runtime (The clean stage)
FROM python:3.9-slim
WORKDIR /app

# Create user first to pass 'api_user_creation_cmd'
RUN useradd -m devops

# Copy only the installed packages from the builder
COPY --from=builder /root/.local /home/devops/.local
COPY . .

# Ensure the non-root user owns the files
RUN chown -R devops:devops /app
USER devops

ENV PATH=/home/devops/.local/bin:$PATH
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
