import aiomysql
from argon2 import PasswordHasher
from shared.errors.auth_errors import EmailError,UserNameError
from shared.errors.db_errors import DbError
from shared.utils.send_links import send_link
from shared.utils.users_attempts import check_rate_limit
from users.utils.validator import check_user_exists,check_email_exists


class RegisterServices:
    def __init__(self,connection,redis,language):
        self.connection = connection
        self.redis = redis
        self.language = language
        self.password_hasher = PasswordHasher()
    #     register
    async def register(self,user_name,email,password,template,background_task):
        try :
            await check_rate_limit(identifier=email,action_type="register",number_attempts=5,time=60,error_content=self.language["rate_limit"]["signup_exceeded"],redis=self.redis)
            if await check_email_exists(email=email,connection=self.connection):
                raise EmailError(self.language["auth"]["email"]["taken"])

            if await check_user_exists(username=user_name,connection=self.connection):
                raise UserNameError(self.language["auth"]["user_name"]["taken"])

            hashed_password = self.password_hasher.hash(password=password)
            async with self.connection.cursor() as cursor:
                await cursor.execute("INSERT INTO `users`(`user_name`,`email`,`password`)VALUES(%s,%s,%s)",(user_name,email,hashed_password))
                await  self.connection.commit()
                # await send_link(email=email,title="verify_account",redis=self.redis,jinja2=template)
                background_task.add_task(send_link,email=email,title="verify_account",redis=self.redis,jinja2=template )

                return {
                    "success": True,
                    "message" : self.language["auth"]["success"]["registered"],
                    "is_verified" : False,
                    "verification_link":self.language["auth"]["links"]["verification_sent"]
                }
        except aiomysql.Error as e:
            await  self.connection.rollback()
            raise DbError(f"database error : {str(e)}")

    # Verify account
    async def verify_account(self,token):
        try :
            redis_key = f"auth:verify_account:{token}"
            email = await self.redis.get(redis_key)
            await check_rate_limit(identifier=email,action_type="verify_account",number_attempts=3,time=60*5,error_content=self.language["rate_limit"]["general"],redis=self.redis)

            if not await check_email_exists(email=email,connection=self.connection):
                raise EmailError(self.language["auth"]["links"]["invalid"])

            async with self.connection.cursor() as cursor:
                await  cursor.execute("UPDATE `users` SET `is_verified` = TRUE WHERE `email` = %s",(email,))
                await self.connection.commit()
                await self.redis.delete(redis_key)
                return {
                    "success": True,
                    "message" : self.language["auth"]["success"]["email_verified"],
                }

        except aiomysql.Error as e:
            await  self.connection.rollback()
            raise DbError(f"database error : {str(e)}")



