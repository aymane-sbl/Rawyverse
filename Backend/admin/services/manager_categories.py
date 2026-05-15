

import aiomysql


from admin.utils.validator import check_categories_is_exists, check_is_admin
from shared.errors.categories_errors import CategoriesError
from shared.errors.db_errors import DbError


class ManagerCategories:
    def __init__(self,lang,connection,redis):
        self.lang = lang
        self.connection = connection
        self.redis = redis
    # add categories
    async def add_categories(self,category_name,payload):
        check_is_admin(payload=payload,lang=self.lang)
        if await check_categories_is_exists(connection=self.connection ,category_name=category_name):
            raise CategoriesError(self.lang["admin"]["categories"]["already_exists"])
        try :
            async with self.connection.cursor() as cursor:
                await cursor.execute("INSERT INTO categories(`category_name`)VALUES (%s)",(category_name,))
                await self.connection.commit()
                return {
                    "success": True,
                    "msg": self.lang["admin"]["categories"]["created"]
                }
        except aiomysql.Error as e:
            await  self.connection.rollback()
            raise DbError(f"database error : {str(e)}")
    # remove category
    async def remove_categories(self,category_name,payload):
        check_is_admin(payload=payload, lang=self.lang)
        if not await check_categories_is_exists(connection=self.connection, category_name=category_name):
            raise CategoriesError(self.lang["admin"]["categories"]["not_found"])
        try :
            async with self.connection.cursor() as cursor:
                await  cursor.execute("DELETE FROM `categories` WHERE `category_name` = %s",(category_name,))
                await self.connection.commit()
                return {
                    "success": True,
                    "msg": self.lang["admin"]["categories"]["deleted"]
                }
        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"database error : {str(e)}")

    # get categories
    async def get_categories(self,payload):
        check_is_admin(payload=payload, lang=self.lang)
        try  :
            async with self.connection.cursor() as cursor:
                await cursor.execute("SELECT `categories_id`,`category_name` FROM `categories`")
                data =await cursor.fetchall()
                return {
                    "success": True,
                    "data": data
                }
        except aiomysql.Error as e:
            await self.connection.rollback()
            raise DbError(f"database error : {str(e)}")