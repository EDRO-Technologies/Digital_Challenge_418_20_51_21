from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.sqlalchemy_db.models.base import Base

if TYPE_CHECKING:
    from app.adapters.sqlalchemy_db.models.object_type import ObjectTypeModel
    from app.adapters.sqlalchemy_db.models.well import WellModel


class ObjectModel(Base):
    __tablename__ = "objects"

    id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, unique=True
    )
    name: Mapped[str] = mapped_column(String(42))
    type: Mapped[int] = mapped_column(
        ForeignKey("objects_type.id", ondelete="CASCADE")
    )

    type_model: Mapped["ObjectTypeModel"] = relationship(
        foreign_keys=[type], uselist=False, back_populates="object_models"
    )
    well_model: Mapped["WellModel"] = relationship(
        back_populates="object_model", uselist=False
    )
