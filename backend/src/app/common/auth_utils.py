from datetime import UTC, datetime, timedelta

import bcrypt
import jwt

from app.common.settings import settings


def jwt_encode(
    payload: dict,
    expire_time_seconds: int,
    private_key: str = settings.auth_settings.PRIVATE_KEY.read_text(),
    algorithm: str = settings.auth_settings.ALGORITHM,
) -> str:
    expire_time = datetime.now(UTC) + timedelta(seconds=expire_time_seconds)
    payload.update(exp=expire_time)
    encoded_jwt_token = jwt.encode(
        payload=payload, key=private_key, algorithm=algorithm
    )
    return encoded_jwt_token


def jwt_decode(
    token: str,
    public_key: str = settings.auth_settings.PUBLIC_KEY.read_text(),
    algorithm: str = settings.auth_settings.ALGORITHM,
) -> dict:
    decoded_jwt_token = jwt.decode(
        jwt=token, key=public_key, algorithms=[algorithm]
    )
    return decoded_jwt_token


def is_valid_password(unhashed_password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(unhashed_password.encode(), hashed_password)


def hash_password(unhashed_password: str) -> bytes:
    return bcrypt.hashpw(unhashed_password.encode(), bcrypt.gensalt())
