import json
from math import ceil
import aiomysql

from shared.errors.db_errors import DbError
from shared.errors.items_errors import ItemsError
from shared.services.utils.check_title import check_books_is_exists


class ManagerPublicItems:
    def __init__(self,connection,redis,lang):
        self.connection = connection
        self.redis = redis
        self.lang = lang
    async def get_items(self,page,limit_items):
        try :
            async with self.connection.cursor() as cursor:
                    # items count
                    await cursor.execute("SELECT COUNT(`id`) as items_count FROM `books` ")
                    items_count = await cursor.fetchone()
                    # get data
                    skip = (page-1)*limit_items
                    await cursor.execute("SELECT id,title,author,category_id,image_url,language,year,pages,file_url,genres,synopsis,created_at  FROM `books` LIMIT %s OFFSET %s",(limit_items,skip))
                    data = await cursor.fetchall()
                    for item in data:
                        for key,value in item.items():
                            if key == "genres":
                                item["genres"]=json.loads(value)
                                break

                    return {
                        "success": True,
                        "pagination": {
                            "current_page": page,
                            "items_count": items_count["items_count"],
                            "limit_items": limit_items,
                            "skip": skip,
                            "total_pages": ceil(items_count["items_count"]/limit_items)
                        },
                        "data": data
                    }


        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"error database : {e}")
    # get items by id
    async def get_items_by_id(self,id):

        try:
            async with self.connection.cursor() as cursor:
                await cursor.execute(
                    "SELECT id,title,author,category_id,image_url,language,year,pages,file_url,genres,synopsis FROM `books` WHERE `id` = %s ",
                    (id,))
                data = await cursor.fetchone()


                if not data:
                    raise ItemsError(self.lang["items"]["invalid_id"])

                if "genres" in data:
                    data["genres"]=json.loads(data["genres"])
                return {
                    "success": True,
                    "data": data
                }
        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"error database : {e}")
    # search
    async def search(self,title):
        if not await check_books_is_exists(title=title ,connection=self.connection):
            raise ItemsError(self.lang["items"]["no_results"])
        try:
            async with self.connection.cursor() as cursor:
                search_template = f"%{title}%"
                await  cursor.execute("SELECT id,title,author,category_id,image_url,language,year,pages,file_url,genres,synopsis FROM `books` WHERE `title` LIKE %s ",(search_template,))
                data = await cursor.fetchall()
                return {
                    "success": True,
                    "data": data
                }
        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"error database : {e}")