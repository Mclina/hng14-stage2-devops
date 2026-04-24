import os
import redis
from fastapi import FastAPI

app = FastAPI()

# Discovery: Use 'redis' as the hostname for Docker
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, db=0)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/submit")
def submit():
    # Your logic to push to 'job_queue'
    return {"status": "job submitted"}
