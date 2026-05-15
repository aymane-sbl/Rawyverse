from fastapi import HTTPException,Request,status
from fastapi.security import OAuth2PasswordBearer
class OAuth2PasswordBearerCookies(OAuth2PasswordBearer):
    def __call__(self,request:Request):
        token = request.cookies.get("access_token")
        if not token:
            if self.auto_error:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Authentication token is missing.")
            return None
        return token
