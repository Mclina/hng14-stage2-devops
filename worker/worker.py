import redis
import time
import os
import signal

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0)

def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)  # simulate work
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")

if __name__ == "__main__":
    print("Worker started. Waiting for jobs...")
while True:
        job = r.brpop("job", timeout=5)
        if job:
            # job[0] is the queue name, job[1] is the byte-string ID
            raw_job_id = job[1] 
            decoded_id = raw_job_id.decode('utf-8')
            process_job(decoded_id)
