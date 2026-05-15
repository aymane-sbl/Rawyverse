from fastapi import Request
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import json



class IpRateLimit(BaseHTTPMiddleware):
    async def dispatch(self,request: Request,call_next):
        ip = request.client.host
        redis = request.app.state.redis
        redis_key = f"rate_limit:ip_attempts:{ip}"
        lang = await redis.get("translations:lang")
        data = json.loads(lang)
        allowed_endpoints = {
            route.path for route in request.app.routes
            if isinstance(route, APIRoute)
        }


        if request.url.path in allowed_endpoints:
            ip_attempts = await redis.incr(redis_key)
            if ip_attempts == 1:
                await redis.expire(redis_key, 60)
            if ip_attempts > 50:
                return JSONResponse(
                    status_code=429,
                    content={"detail":data["rate_limit"]["ip_blocked"]}
                )

        response = await call_next(request)
        return response
