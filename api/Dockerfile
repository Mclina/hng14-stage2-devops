# Stage 1: Build
FROM python:3.9-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim
WORKDIR /app
RUN useradd -m devops
COPY --from=builder /root/.local /home/devops/.local
COPY . .
RUN chown -R devops:devops /app
USER devops
ENV PATH=/home/devops/.local/bin:$PATH
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
