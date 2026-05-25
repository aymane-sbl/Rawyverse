
import aiomysql
import json

from admin.utils.get_lenght_table import get_lenght_table
from admin.utils.validator import check_is_admin, check_books_is_exists
from shared.errors.db_errors import DbError
from shared.errors.items_errors import ItemsError


from shared.utils.config_s3 import  aws_upload_file_and_rename_name,aws_upload_file_and_full_rename


class ManagerItems :
    def __init__(self,connection,redis,lang):
        self.connection = connection
        self.redis = redis
        self.lang = lang


    async def __get_specific_item(self,category_id):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                "SELECT COUNT(`id`) as count FROM `books` WHERE `category_id` = %s", (category_id,))
            data = await cursor.fetchone()
            return {
                "success": True,
                "length": data["count"]
            }

    #    add items
    async def add_items(self,payload,title,author,category_id,image,language,year,pages,file_url,genres,synopsis):
        check_is_admin(payload=payload,lang=self.lang)
        if await check_books_is_exists(connection=self.connection,title=title):
            raise ItemsError(self.lang["items"]["already_exists"])
        try :
            async with self.connection.cursor() as cursor:
                # upload image

                image_link = aws_upload_file_and_full_rename(files=image,path=f"items/images",lang=self.lang)
                # upload file
                file_link = aws_upload_file_and_rename_name(files=file_url,path=f"items/files",lang=self.lang)
                # genres
                str_genres_list = json.dumps(genres.split(","))


                await cursor.execute("""
                    INSERT INTO `books`(title,author,category_id,image_url,language,year,pages,file_url,genres,synopsis)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,(title,author,category_id,image_link,language,year,pages,file_link,str_genres_list,synopsis))
                await self.connection.commit()

                return {
                    "success": True,
                    "msg":self.lang["items"]["added"]
                }

        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"error database : {e}")
    # delete item
    async def remove_items(self,title,payload):
        check_is_admin(payload=payload,lang=self.lang)
        if not await check_books_is_exists(title=title,connection=self.connection):
            raise ItemsError(self.lang["items"]["not_found"])
        try :
            async with self.connection.cursor() as cursor:
                await cursor.execute("DELETE FROM `books` WHERE `title` = %s",(title,))
                await self.connection.commit()
                return {
                    "success": True,
                    "msg":self.lang["items"]["deleted"]
                }
        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"error database : {e}")

    async def length_table(self):
        try:
            return await get_lenght_table(connection=self.connection,table="books",column="id")
        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"error database : {e}")


        #     get length books
    async def get_length_books(self):
        try:
            return await self.__get_specific_item(category_id=1)
        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"error database : {e}")

    async def get_length_novels(self):
        try:
            return await self.__get_specific_item(category_id=2)
        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"error database : {e}")









