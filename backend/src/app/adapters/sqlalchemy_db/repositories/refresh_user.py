from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.sqlalchemy_db.models.refresh_user import RefreshUserModel
from app.ports.repositories.refresh_user import RefreshUserRepository


class SqlalRefreshUserReporitory(RefreshUserRepository):
    _model = RefreshUserModel

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_user_white_ip_list(self, user_id: UUID):
        query = select(self._model.white_ip_list).where(
            self._model.user_id == user_id
        )
        result = await self._session.execute(query)
        return result.scalar_one_or_none()

    async def add_ip_to_white_ip_list(
        self, user_id: UUID, white_ip_list: set[str]
    ) -> UUID | None:
        stmt = (
            update(self._model)
            .where(self._model.user_id == user_id)
            .values({"white_ip_list": list(white_ip_list)})
            .returning(self._model.id)
        )
        refresh_user_id = await self._session.execute(stmt)
        refresh_user_id = refresh_user_id.scalar_one_or_none()
        return refresh_user_id

    async def get_user_by_id(self, user_id: UUID):
        query = (
            select(self._model)
            .where(self._model.user_id == user_id)
            .options(selectinload(self._model.refresh_tokens_model))
        )
        result = await self._session.execute(query)
        return result.scalar_one_or_none()

    async def delete_by_refresh_user_id(
        self, refresh_user_id: UUID, token: str
    ) -> None:
        stmt = delete(self._model).where(
            self._model.refresh_user_id == refresh_user_id
        )
        await self._session.execute(stmt)
