from shared.errors.users_errors import UsersError


class LogoutServices:
    def __init__(self,connection,redis,lang):
        self.connection = connection
        self.redis = redis
        self.language = lang
    async def logout(self,response):
        try :
            response.delete_cookie(
                key="access_token",
                httponly=True,
                secure=False,
                samesite="lax"
            )
            return {
                "success": True,
                "msg":self.language["auth"]["logout"]["success"]
            }
        except Exception:
            raise UsersError(self.language["auth"]["logout"]["failed"])
