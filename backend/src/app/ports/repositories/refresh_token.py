from abc import ABC, abstractmethod
from typing import NoReturn
from uuid import UUID


class RefreshTokenRepository(ABC):
    @abstractmethod
    async def add_one_token(self, token: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_refresh_token(self, refresh_token: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_refresh_user_id_and_token(
        self, refresh_user_id: UUID, refresh_token: str
    ) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_refresh_user_id(
        self, refresh_user_id: UUID
    ) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def delete_one_by_id(self, refresh_token_id: UUID) -> NoReturn:
        raise NotImplementedError
