
import uvicorn
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache
import redis.asyncio as redis_as
from contextlib import asynccontextmanager
import firebase_admin
from starlette.middleware.cors import CORSMiddleware

from shared.database.database import Database
from shared.database.redis_cache import init_redis_cache
from shared.middelware.ip_rate_limit import IpRateLimit
from shared.models.init_tables import init_tables
from shared.utils.set_lange_redis import set_lange_redis
from users.router import auth
from admin.router import categories,items,users
from shared.router.items_public_router import router as items_public_router

load_dotenv(override=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # init database
    db = Database()
    pool =await db.create_pool()
    app.state.pool = pool
#     init redis
    redis = redis_as.from_url(os.getenv("REDIS_URL"),decode_responses=True)
    app.state.redis = redis
#   init redis cache
    init_redis_cache(redis=redis, redis_backend=RedisBackend ,fast_api_cache=FastAPICache)

# init tables
    async with app.state.pool.acquire() as connection:
        await init_tables(connection=connection)
    # init language
    await set_lange_redis(redis=app.state.redis,file="ar.json")
    # init firebase
    credential = firebase_admin.credentials.Certificate("./firebase/serviceAccountKey.json")
    firebase_admin.initialize_app(credential=credential)

    yield
    pool.close()
    await pool.wait_closed()

app = FastAPI(lifespan=lifespan)
# middleware
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost:63343",
    "http://127.0.0.1:63343",
    "https://rawyverse.pages.dev/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(IpRateLimit)

@app.get("/")
def read_root():
    return {
            "welcome": "welcome to my api",
            "docs":"/docs",
            "Github":"https://github.com/aymane-sbl"
            }

# users
app.include_router(auth.router)

# admin
app.include_router(categories.router)
app.include_router(items.router)
app.include_router(items_public_router)

app.include_router(users.router)
if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)