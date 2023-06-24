import os

import jwt


class JWTService:
    def __init__(self):
        jwt_secret = os.environ.get("JWT_SECRET") or "JWT_SECRET"
        encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
