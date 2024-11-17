from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.sqlalchemy_db.models.user import UserModel
from app.dto.user import DatabaseUser
from app.ports.repositories.user import UserRepository


class SqlalUserRepository(UserRepository):
    _model = UserModel

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_user_by_user_login(self, login: str) -> DatabaseUser | None:
        query = select(self._model).where(self._model.login == login)
        user = await self._session.execute(query)
        user = user.scalar_one_or_none()
        return (
            DatabaseUser(id=user.id, login=user.login, password=user.password)
            if user
            else None
        )

    async def get_user_by_user_id(self, user_id: UUID) -> DatabaseUser | None:
        query = select(self._model).where(self._model.id == user_id)
        user = await self._session.execute(query)
        user = user.scalar_one_or_none()
        return (
            DatabaseUser(id=user.id, login=user.login, password=user.password)
            if user
            else None
        )
