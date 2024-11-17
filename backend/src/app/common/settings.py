from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    title: str = "dc2024"
    debug: bool = True
    allow_origins: list[str]
    api_v1_prefix: str = "/api/v1"
    docs_url: str | None = "/api/docs"
    openapi_url: str | None = "/api/openapi.json"
    app_url: str = "https://localhost/"

    class Config:
        env_file = ".env"
        env_prefix = "app_"


class PostgresSettings(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    db: str

    echo: bool = True
    pool_size: int = 15
    max_overflow: int = 15

    class Config:
        env_file = ".env"
        env_prefix = "postgres_"
        case_sensetive = False


class AuthSettings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60
    REFRESH_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7
    ALGORITHM: str = "RS256"
    PUBLIC_KEY: Path = (
        Path(__file__).parent.parent.parent.parent
        / "private_keys"
        / "jwt-public.pem"
    )
    PRIVATE_KEY: Path = (
        Path(__file__).parent.parent.parent.parent
        / "private_keys"
        / "jwt-private.pem"
    )


class Settings:
    app_settings = AppSettings()  # pyright: ignore[reportCallIssue]
    auth_settings = AuthSettings()  # pyright: ignore[reportCallIssue]
    postgres_settings = PostgresSettings()  # pyright: ignore[reportCallIssue]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
