from fastapi import Request, HTTPException
from app.api.rate_limit import rate_limit

def rate_limit_dep(request: Request):
    try:
        rate_limit(request.client.host)
    except Exception:
        raise HTTPException(status_code=429, detail="Too many requests")
