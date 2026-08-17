from datetime import datetime, timezone, timedelta
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv("SECRET_KEY")

def generate_access_token(username: str):
    now = datetime.now(timezone.utc)
    
    exprie_time = now + timedelta(minutes=30)
    
    payload = {
        "sub": username,
        "iat": now.timestamp(),
        "exp": exprie_time
    }
    
    
    return jwt.encode(payload, key=secret_key, algorithm="HS256")

def jwt_decode(token: str):
    return jwt.decode(token, secret_key, algorithms=["HS256"])
