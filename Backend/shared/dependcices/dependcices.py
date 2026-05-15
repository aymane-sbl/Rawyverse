import aiomysql
from fastapi import Depends
from typing import Annotated
from redis.asyncio import Redis

from shared.dependcices import get_connection_db, get_coonection_redis
from shared.dependcices.get_lang_redis import get_lang_redis


conn_dep = Annotated[aiomysql.Pool,Depends(get_connection_db.get_connection)]
redis_dep = Annotated[Redis,Depends(get_coonection_redis.get_connection_redis)]
lang_dep = Annotated[dict,Depends(get_lang_redis)]
