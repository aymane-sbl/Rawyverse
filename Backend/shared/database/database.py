import os
import aiomysql
from dotenv import load_dotenv
load_dotenv(override=True)
class Database:
    ssl_ctx = ssl.create_default_context()
    async def create_pool(self):
        pool = await aiomysql.create_pool(
            host =os.getenv("HOST"),
            user =os.getenv("USER"),
            password =os.getenv("PASSWORD"),
            port = int(os.getenv("DB_PORT")) ,
            db=os.getenv("DB"),
            autocommit = True,
            minsize=5,
            maxsize=32,
            cursorclass=aiomysql.DictCursor,
            init_command="SET time_zone = '+00:00'"
            ssl=ssl_ctx
        )
        return pool