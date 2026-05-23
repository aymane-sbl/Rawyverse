import aiomysql

from shared.errors.db_errors import DbError
from shared.errors.users_errors import UsersError


class ProfileService:
    def __init__(self,connection,redis,lang):
        self.connection = connection
        self.redis = redis
        self.lang = lang
    async def get_user_profile(self,email):
        try:
            async with self.connection.cursor() as cursor:
                await cursor.execute("SELECT `user_name`,`email` FROM `users` WHERE `email` = %s", (email,))
                data = await cursor.fetchone()
                if not data:
                    raise UsersError(self.lang["users"]["not_found"])
                return {
                    "user_name": data["user_name"],
                    "email": data["email"]
                }
        except aiomysql.Error as e:
            await  self.connection.rollback()
            raise DbError(f"database error : {str(e)}")
