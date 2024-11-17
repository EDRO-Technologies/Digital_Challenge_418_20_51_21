from abc import ABC, abstractmethod
from uuid import UUID

from app.dto.user import DatabaseUser


class UserRepository(ABC):
    @abstractmethod
    async def get_user_by_user_login(self, login: str) -> DatabaseUser | None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_user_id(self, user_id: UUID) -> DatabaseUser | None:
        raise NotImplementedError
