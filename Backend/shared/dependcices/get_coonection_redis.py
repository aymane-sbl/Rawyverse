from fastapi import Request
async def get_connection_redis(request: Request):
    redis =request.app.state.redis
    return redis