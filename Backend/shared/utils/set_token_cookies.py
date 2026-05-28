from shared.utils.securite import encode_token
from datetime import datetime,timedelta,timezone

def create_token_cookies(email,role,response):
    payload = {"sub": email,"role":role, "exp": datetime.now(timezone.utc) + timedelta(minutes=20)}
    token = encode_token(payload)
    response.set_cookie(key="access_token", value=token, httponly=True, secure=True, samesite="none", max_age=1800)