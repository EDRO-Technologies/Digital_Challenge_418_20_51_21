from abc import ABC, abstractmethod
from typing import Self

from app.ports.repositories.refresh_token import RefreshTokenRepository
from app.ports.repositories.refresh_user import RefreshUserRepository
from app.ports.repositories.user import UserRepository
from app.ports.repositories.well_day import WellDayRepository


class UoW(ABC):
    refresh_tokens: RefreshTokenRepository
    refresh_users: RefreshUserRepository
    users: UserRepository
    well_day: WellDayRepository

    @abstractmethod
    async def __aenter__(self) -> Self:
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args: tuple) -> None:  # pyright: ignore[reportUnknownParameterType, reportMissingTypeArgument]
        raise NotImplementedError

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError
