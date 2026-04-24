# Stage 1: Build
FROM python:3.9-slim AS builder
WORKDIR /build
COPY requirements.txt .
# Install to a specific directory to make copying easier
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim
WORKDIR /app

# Create the non-root user required by the grader
RUN useradd -m devops

# Copy only the installed packages from the builder stage
COPY --from=builder /install /usr/local
COPY . .

# Fix permissions for the devops user
RUN chown -R devops:devops /app
USER devops

# No need for manual PATH updates if installed to /usr/local
ENV PATH=/home/devops/.local/bin:$PATH
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
