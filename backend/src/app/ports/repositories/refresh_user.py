from abc import ABC, abstractmethod
from typing import NoReturn
from uuid import UUID


class RefreshUserRepository(ABC):
    @abstractmethod
    async def get_user_white_ip_list(self, user_id: UUID) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def add_ip_to_white_ip_list(
        self, user_id: UUID, white_ip_list: set[str]
    ) -> UUID:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_id(self, user_id: UUID) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_refresh_user_id(
        self, refresh_user_id: UUID, token: str
    ) -> NoReturn:
        raise NotImplementedError
