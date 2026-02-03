# app/api/rate_limit.py
import time
from collections import defaultdict
from typing import DefaultDict, List

WINDOW = 60
MAX_REQUESTS = 30

_requests: DefaultDict[str, List[float]] = defaultdict(list)


def rate_limit(key: str) -> None:
    now = time.time()
    _requests[key] = [t for t in _requests[key] if t > now - WINDOW]

    if len(_requests[key]) >= MAX_REQUESTS:
        raise Exception("Rate limit exceeded")

    _requests[key].append(now)
