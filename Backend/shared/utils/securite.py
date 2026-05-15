import jwt
import os
from dotenv import load_dotenv

load_dotenv(override=True)
def encode_token(payload):
    token = jwt.encode(payload=payload,key=os.getenv("SECRET_TOKEN"), algorithm="HS256")
    return token



