from fastapi import Request
import json
async def get_lang_redis(request: Request):
    redis = request.app.state.redis
    lang = await redis.get("translations:lang")
    data = json.loads(lang)
    return data