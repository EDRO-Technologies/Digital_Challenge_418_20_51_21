from uuid import UUID

from app.dto.user import User
from app.ports.uow import UoW


class UserService:
    async def get_one_by_id(self, user_id: UUID, uow: UoW) -> User | None:
        async with uow:
            user = await uow.users.get_user_by_user_id(user_id)
            return user
