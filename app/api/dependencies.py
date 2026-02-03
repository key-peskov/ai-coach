# app/api/dependencies.py
from fastapi import HTTPException, Request

from app.api.rate_limit import rate_limit


def rate_limit_dep(request: Request) -> None:
    client = request.client
    if client is None:
        raise HTTPException(status_code=400, detail="Cannot determine client")

    try:
        rate_limit(client.host)
    except Exception:
        raise HTTPException(status_code=429, detail="Too many requests")
