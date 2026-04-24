import os
import redis
import time

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, db=0)

while True:
    job = r.brpop("job_queue", timeout=5)
    if job:
        job_id = job[1].decode('utf-8') # Crucial Fix: Decode bytes to string
        print(f"Processing {job_id}")
        time.sleep(2)
        r.set(f"status:{job_id}", "completed")
