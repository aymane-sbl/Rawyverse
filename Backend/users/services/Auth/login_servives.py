import aiomysql
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from firebase_admin import auth
from firebase_admin.exceptions import FirebaseError

from shared.errors.auth_errors import EmailError, PasswordError, TokenError, FireBaseEr
from shared.errors.db_errors import DbError
from shared.utils.set_token_cookies import create_token_cookies
from shared.utils.users_attempts import check_rate_limit

from shared.utils.validator import check_email_exists



class LoginServices:
    def __init__(self,connection,redis,language,response):
        self.connection = connection
        self.redis = redis
        self.language = language
        self.password_hasher = PasswordHasher()
        self.response = response
    async def login(self,email,password):
        try:
            await check_rate_limit(identifier=email,action_type="login",number_attempts=5,time=60,error_content=self.language["rate_limit"]["login_exceeded"],redis=self.redis)
            if not await check_email_exists(email=email,connection=self.connection):
                raise EmailError(self.language["auth"]["email"]["not_found"])
            async with self.connection.cursor() as cursor:
                await cursor.execute("SELECT `password`,`role` FROM `users` WHERE `email`=%s",(email,))
                data = await cursor.fetchone()
                self.password_hasher.verify(data["password"],password)
                # create token
                create_token_cookies(email=email,role=data["role"],response=self.response)
                return {
                    "success":True,
                    "message" : self.language["auth"]["success"]["logged_in"],
                    "role":data["role"]
                }

        except VerifyMismatchError :
            raise PasswordError(self.language["auth"]["password"]["incorrect"])
        except aiomysql.Error as e:
            await  self.connection.rollback()
            raise DbError(f"database error : {str(e)}")

    # login with google
    async def login_with_google(self,token):

        try :
            decode_token = auth.verify_id_token(token)
            email = decode_token.get("email")
            await check_rate_limit(identifier=email,action_type="login",number_attempts=5,time=60,error_content=self.language["rate_limit"]["login_exceeded"],redis=self.redis)
            user_exists = await check_email_exists(email=email,connection=self.connection)

            async with self.connection.cursor() as cursor:
                if not user_exists:
                    await cursor.execute("INSERT INTO `users`(`email`)VALUES(%s)",(email,))
                    await self.connection.commit()
                else :
                    await cursor.execute("UPDATE `users` SET `is_verified` = TRUE WHERE `email` = %s", (email,))
                    await self.connection.commit()
                # create token
                create_token_cookies(email=email, response=self.response)
                return {
                    "success": True,
                    "message": self.language["auth"]["success"]["logged_in"],
                }
        except auth.InvalidIdTokenError :
            raise TokenError(self.language["auth"]["invalid_id_token"]["incorrect"])
        except auth.ExpiredIdTokenError :
            raise TokenError(self.language["auth"]["expired_id_token"]["expired"])
        except auth.RevokedIdTokenError :
            raise TokenError(self.language["auth"]["success"]["logged_out"])
        except FirebaseError as e :
            raise FireBaseEr(f"Firebase Error : {e}")
        except aiomysql.Error as e:
            await  self.connection.rollback()
            raise DbError(f"database error : {str(e)}")
