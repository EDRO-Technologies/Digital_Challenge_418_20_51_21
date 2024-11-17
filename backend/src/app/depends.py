from functools import partial
from typing import Annotated
from uuid import UUID

import jwt
from fastapi import Depends, FastAPI, Request
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.adapters.sqlalchemy_db.uow import SqlalUoW
from app.common.auth_utils import jwt_decode
from app.common.exceptions import InvalidToken, NotAuthenticated
from app.common.settings import PostgresSettings, settings
from app.dto.user import User
from app.ports.uow import UoW
from app.services.auth import AuthService
from app.services.user import UserService
from app.services.well_day import WellDayService


def create_async_sessionmaker(
    settings: PostgresSettings,
) -> async_sessionmaker[AsyncSession]:
    postgres_dsn: URL = URL.create(
        drivername="postgresql+asyncpg",
        username=settings.user,
        password=settings.password,
        host=settings.host,
        port=settings.port,
        database=settings.db,
    )

    async_engine: AsyncEngine = create_async_engine(
        url=postgres_dsn,
        echo=settings.echo,
        pool_size=settings.pool_size,
        max_overflow=settings.max_overflow,
    )
    return async_sessionmaker(async_engine, expire_on_commit=False)


def create_uow(
    async_session_maker: async_sessionmaker[AsyncSession],
) -> SqlalUoW:
    return SqlalUoW(async_session_maker)


def create_auth_service() -> AuthService:
    return AuthService()


def create_user_service() -> UserService:
    return UserService()


def create_well_day_service() -> WellDayService:
    return WellDayService()


async def get_access_from_cookie(request: Request) -> str:
    if access_token := request.cookies.get("access_token"):
        return access_token
    raise NotAuthenticated


async def get_current_user(
    uow: Annotated[UoW, Depends()],
    service: Annotated[UserService, Depends()],
    access_token: str = Depends(get_access_from_cookie),
) -> User:
    try:
        user = jwt_decode(access_token)
        user = await service.get_one_by_id(UUID(user.get("sub")), uow)
        if user is None:
            raise InvalidToken
    except jwt.InvalidTokenError:
        raise InvalidToken
    return user


def init_depends(app: FastAPI) -> None:
    async_session_maker = create_async_sessionmaker(settings.postgres_settings)

    app.dependency_overrides[UoW] = partial(
        create_uow,
        async_session_maker,
    )
    app.dependency_overrides[AuthService] = create_auth_service
    app.dependency_overrides[UserService] = create_user_service
