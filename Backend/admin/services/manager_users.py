import aiomysql

from admin.utils.validator import check_is_admin

from shared.errors.db_errors import DbError
from shared.errors.users_errors import UsersError
from shared.utils.validator import check_email_exists


class ManagerUsersService:
    def __init__(self,connectin,redis,lang):
        self.connectin = connectin
        self.redis = redis
        self.lang = lang

    # get all users
    async def get_all_users(self):
        try :
            async with self.connectin.cursor() as cursor:
                await cursor.execute("select `id`,`user_name`, `email`, `is_verified`,`role`,`created_at` from users ORDER BY (`id`) DESC")
                data = await cursor.fetchall()
                return {
                    "success": True,
                    "data": data
                }
        except aiomysql.Error as e:
            await self.connectin.rollback()
            raise DbError(f"error : {e}")

    # delete users
    async def  delete_user(self,email,payload):
        check_is_admin(payload=payload,lang=self.lang)
        try :
            if not await check_email_exists(email,self.connectin):
                raise UsersError(self.lang["admin"]["users_management"]["not_found"])
            async with self.connectin.cursor() as cursor:
                await cursor.execute("DELETE FROM users WHERE email = %s", (email,))
                await self.connectin.commit()
                return {
                    "success": True,
                    "msg": self.lang["admin"]["users_management"]["deleted"]
                }
        except aiomysql.Error as e:
            await self.connectin.rollback()
            raise DbError(f"error : {e}")

