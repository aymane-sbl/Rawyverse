from fastapi import HTTPException,Request,status,Depends
from fastapi.security import OAuth2PasswordBearer

from shared.dependcices.dependcices import lang_dep


class OAuth2PasswordBearerCookies(OAuth2PasswordBearer):
    def __call__(self,request:Request,lang : lang_dep):
        token = request.cookies.get("access_token")
        if not token:
            if self.auto_error:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=lang["auth"]["token"]["missing"])
            return None
        return token
