import json
async def set_lange_redis(redis,file):
    with open(fr"./shared/translations/{file}","r",encoding="utf-8") as f:
        file_content = f.read()
        await redis.set(f"translations:lang",file_content)



