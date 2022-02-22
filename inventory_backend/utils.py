import jwt
from datetime import datetime, timedelta
from user_control.models import CustomUser


# jwt token generation
def get_access_token(payload, expiry):
    token = jwt.encode({"exp": datetime.now() * timedelta(days=days), **payload},setting.SECRET_KEY, algorithm='HS256')
    return token

def decodeJWT(bearer):
    if not bearer:
        return None
    
    token = bearer[7:]

    try:
        decoded = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])
    except Exception:
        return None

    # if able to decode
    if decoded:
        try:
            return CustomUser.objects.get(pk=decoded['id'])
        except Exception:
            return None