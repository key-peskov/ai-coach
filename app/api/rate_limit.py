import time
from collections import defaultdict

WINDOW = 60
MAX_REQUESTS = 30
_requests = defaultdict(list)

def rate_limit(key: str):
    now = time.time()
    _requests[key] = [t for t in _requests[key] if t > now - WINDOW]
    if len(_requests[key]) >= MAX_REQUESTS:
        raise Exception("Rate limit exceeded")
    _requests[key].append(now)
