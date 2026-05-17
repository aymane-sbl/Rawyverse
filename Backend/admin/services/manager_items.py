
import aiomysql
import json

from admin.utils.validator import check_is_admin, check_books_is_exists
from shared.errors.db_errors import DbError
from shared.errors.items_errors import ItemsError


from shared.utils.config_s3 import  aws_upload_file_and_rename_name,aws_upload_file_and_full_rename


class ManagerItems :
    def __init__(self,connection,redis,lang):
        self.connection = connection
        self.redis = redis
        self.lang = lang
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







