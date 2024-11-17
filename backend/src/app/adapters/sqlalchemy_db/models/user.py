import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.sqlalchemy_db.models.base import Base

if TYPE_CHECKING:
    from app.adapters.sqlalchemy_db.models.refresh_user import RefreshUserModel


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(),
        primary_key=True,
        default=uuid.uuid4,
    )
    login: Mapped[str]
    password: Mapped[bytes]

    refresh_user_model: Mapped["RefreshUserModel"] = relationship(
        back_populates="user_model", uselist=True
    )
