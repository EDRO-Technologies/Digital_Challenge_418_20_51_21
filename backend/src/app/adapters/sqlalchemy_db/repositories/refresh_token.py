from uuid import UUID

from sqlalchemy import and_, delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.sqlalchemy_db.models.refresh_token import RefreshTokenModel
from app.ports.repositories.refresh_token import RefreshTokenRepository


class SqlalRefreshTokenReporitory(RefreshTokenRepository):
    _model = RefreshTokenModel

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add_one_token(self, token: dict) -> None:
        stmt = insert(self._model).values(**token)
        await self._session.execute(stmt)

    async def delete_by_refresh_token(self, refresh_token: str) -> None:
        stmt = delete(self._model).where(self._model.token == refresh_token)
        await self._session.execute(stmt)

    async def get_by_refresh_user_id_and_token(
        self, refresh_user_id: UUID, refresh_token: str
    ):
        query = select(self._model).where(
            and_(
                self._model.refresh_user_id == refresh_user_id,
                self._model.token == refresh_token,
            )
        )
        result = await self._session.execute(query)
        return result.scalar_one_or_none()

    async def delete_by_refresh_user_id(
        self,
        refresh_user_id: UUID,
    ) -> None:
        stmt = delete(self._model).where(
            self._model.refresh_user_id == refresh_user_id
        )
        await self._session.execute(stmt)

    async def delete_one_by_id(self, refresh_token_id: UUID) -> None:
        stmt = delete(self._model).where(self._model.id == refresh_token_id)
        await self._session.execute(stmt)
