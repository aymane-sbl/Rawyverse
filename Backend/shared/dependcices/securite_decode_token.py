from fastapi import Depends,HTTPException,status
import jwt
import os

from shared.dependcices.dependcices import lang_dep
from shared.dependcices.get_token_cookies import OAuth2PasswordBearerCookies
oauth2_scheme = OAuth2PasswordBearerCookies(tokenUrl="/api/v1/login")
def decode_token(lang : lang_dep ,token = Depends(oauth2_scheme)):
    try :
        payload = jwt.decode(token, key=os.getenv("SECRET_TOKEN"), algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=lang["auth"]["token"]["expired"])
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=lang["auth"]["token"]["invalid"])