import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.sqlalchemy_db.models.base import Base

if TYPE_CHECKING:
    from app.adapters.sqlalchemy_db.models.refresh_token import (
        RefreshTokenModel,
    )
    from app.adapters.sqlalchemy_db.models.user import UserModel


class RefreshUserModel(Base):
    __tablename__ = "refresh_users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4
    )
    white_ip_list = mapped_column(ARRAY(String), nullable=True)
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="CASCADE")
    )
    refresh_tokens_model: Mapped[list["RefreshTokenModel"]] = relationship(
        back_populates="refresh_user_model"
    )
    user_model: Mapped["UserModel"] = relationship(
        foreign_keys=[user_id],
        uselist=False,
        back_populates="refresh_user_model",
    )
