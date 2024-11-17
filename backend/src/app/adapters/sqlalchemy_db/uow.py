from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.adapters.sqlalchemy_db.repositories.refresh_token import (
    SqlalRefreshTokenReporitory,
)
from app.adapters.sqlalchemy_db.repositories.refresh_user import (
    SqlalRefreshUserReporitory,
)
from app.adapters.sqlalchemy_db.repositories.user import SqlalUserRepository
from app.adapters.sqlalchemy_db.repositories.well_day import (
    SqlalWellDayRepository,
)
from app.ports.uow import UoW


class SqlalUoW(UoW):
    def __init__(
        self,
        async_session_maker: async_sessionmaker[AsyncSession],
    ) -> None:
        self._session_factory = async_session_maker

    async def __aenter__(self) -> Self:
        self._session: AsyncSession = self._session_factory()

        self.refresh_tokens = SqlalRefreshTokenReporitory(self._session)
        self.refresh_users = SqlalRefreshUserReporitory(self._session)
        self.users = SqlalUserRepository(self._session)
        self.well_day = SqlalWellDayRepository(self._session)
        return self

    async def __aexit__(self, *args: tuple) -> None:  # pyright: ignore[reportUnknownParameterType, reportMissingTypeArgument]
        await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
