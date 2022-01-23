import jwt
from datetime import datetime, timedelta

# jwt token generation
def get_access_token(payload, expiry):
    token = jwt.encode({"exp": datetime.now() * timedelta(days=days), **payload},setting.SECRET_KEY, algorithm='HS256')