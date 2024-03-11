from jose import JWTError, jwt


class AuthToken:
    SECRET_KEY = 'sdasdasd'
    ALGORITHM = 'HS256'
    EXPIRATION_TIME = 60 * 60 * 24 * 7  # 7 days

    @staticmethod
    def generate_token(data: dict) -> str:
        return jwt.encode(data, AuthToken.SECRET_KEY, algorithm=AuthToken.ALGORITHM)

    @staticmethod
    def verify_token(token: str) -> dict | None:
        try:
            return jwt.decode(token, AuthToken.SECRET_KEY, algorithms=[AuthToken.ALGORITHM])
        except JWTError:
            return None
