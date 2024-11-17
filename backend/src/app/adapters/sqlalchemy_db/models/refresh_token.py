import datetime
import uuid
from typing import TYPE_CHECKING

from sqlalchemy import TIMESTAMP, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.adapters.sqlalchemy_db.models.base import Base
from app.common.settings import settings

if TYPE_CHECKING:
    from app.adapters.sqlalchemy_db.models.refresh_user import RefreshUserModel


class RefreshTokenModel(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4
    )
    refresh_user_id: Mapped[uuid.UUID] = mapped_column(
        UUID, ForeignKey("refresh_users.id", ondelete="CASCADE")
    )
    token: Mapped[str]
    expire_time_seconds: Mapped[int] = mapped_column(
        default=settings.auth_settings.REFRESH_TOKEN_EXPIRE_SECONDS
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now()
    )
    refresh_user_model: Mapped["RefreshUserModel"] = relationship(
        foreign_keys=[refresh_user_id], back_populates="refresh_tokens_model"
    )
