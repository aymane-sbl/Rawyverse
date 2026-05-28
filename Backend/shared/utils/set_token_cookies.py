from shared.utils.securite import encode_token
from datetime import datetime,timedelta,timezone

def create_token_cookies(email,role,response):
    payload = {"sub": email,"role":role, "exp": datetime.now(timezone.utc) + timedelta(days=30)}
    token = encode_token(payload)
    response.set_cookie(key="access_token", value=token, httponly=True, secure=True, samesite="none", max_age= 30* 24 * 60 * 60)