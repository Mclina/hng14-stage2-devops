# HNG Stage 2 - Bug Fix Log

### 1. API: Connection Logic
- **File:** `api/main.py`
- **Line:** 8
- **Issue:** The Redis host was hardcoded to `localhost`. This works on a local PC but fails inside Docker containers because containers use service names to communicate.
- **Fix:** Replaced `"localhost"` with `os.getenv("REDIS_HOST", "localhost")`.

### 2. API: Missing Dependencies
- **File:** `api/main.py`
- **Line:** 1-4
- **Issue:** Code was using `FastAPI`, `redis`, and `uuid` without importing them, causing a `NameError`.
- **Fix:** Added missing import statements at the top of the file.

### 3. API: Error Handling
- **File:** `api/main.py`
- **Line:** 20-24
- **Issue:** The `get_job` endpoint would crash if a `job_id` didn't exist because it tried to `.decode()` a `None` value.
- **Fix:** Added a conditional check `if status is None` to return a 404 message instead of crashing.
### Worker Service
- **File:** `worker/worker.py`
- **Line:** 18-22
- **Issue:** The Redis `brpop` function returns a tuple `(queue_name, data)`. The original code tried to decode the entire tuple as a string, which causes an `AttributeError`. 
- **Fix:** Implemented tuple unpacking (`_, job_id = job`) and explicit `.decode('utf-8')` on the second element to get the correct Job ID string.

- **Issue:** Redis connection host was hardcoded to `localhost`.
- **Fix:** Replaced with `os.getenv("REDIS_HOST", "localhost")` to allow the worker to find the Redis container in the Docker network.
## Infrastructure & Containerization
- **Issue:** Default Docker containers run as `root`, which is a security risk.
- **Fix:** Implemented `useradd` and `USER` instructions in all Dockerfiles to run processes as non-privileged users.
- **Issue:** Docker images were too large and included unnecessary build tools.
- **Fix:** Used Multi-stage builds to keep final production images slim and efficient.
### 5. Infrastructure: Orchestration & Healthchecks
* **File:** `docker-compose.yml`
* **Issue:** Race conditions occurred where the API and Worker attempted to connect to Redis before the database was fully initialized, leading to "Connection Refused" errors.
* **Fix:** Implemented a native Docker `healthcheck` for the Redis service and configured the `api` and `worker` services with `depends_on: condition: service_healthy`. This ensures a synchronized startup sequence.

### 6. Infrastructure: YAML Syntax & Standards
* **File:** `docker-compose.yml`
* **Issue:** Improper indentation and block mapping errors (specifically regarding the `deploy` and `networks` keys) prevented the stack from deploying.
* **Fix:** Re-aligned all service properties to follow strict YAML 1.2 standards and validated the configuration using `docker compose config` to ensure a valid schema.
