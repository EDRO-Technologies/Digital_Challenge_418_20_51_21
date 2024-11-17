from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.sqlalchemy_db.models.base import Base

if TYPE_CHECKING:
    from app.adapters.sqlalchemy_db.models import ObjectModel


class ObjectTypeModel(Base):
    __tablename__ = "objects_type"

    id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, unique=True
    )
    name: Mapped[str] = mapped_column(String(42))

    object_models: Mapped[list["ObjectModel"]] = relationship(
        back_populates="type_model",
        uselist=True,
    )
