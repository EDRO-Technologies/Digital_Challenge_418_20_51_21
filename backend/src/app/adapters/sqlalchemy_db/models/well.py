from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.sqlalchemy_db.models.base import Base

if TYPE_CHECKING:
    from app.adapters.sqlalchemy_db.models.object import ObjectModel
    from app.adapters.sqlalchemy_db.models.well_day_history import (
        WellDayHistoryModel,
    )
    from app.adapters.sqlalchemy_db.models.well_day_plan import (
        WellDayPlanModel,
    )


class WellModel(Base):
    __tablename__ = "wells"

    well: Mapped[int] = mapped_column(
        ForeignKey("objects.id"), primary_key=True
    )
    ngdu: Mapped[int]
    cdng: Mapped[int]
    kust: Mapped[int]
    mest: Mapped[int]

    object_model: Mapped["ObjectModel"] = relationship(
        foreign_keys=[well],
        uselist=False,
        back_populates="well_model",
    )
    well_day_history_model: Mapped["WellDayHistoryModel"] = relationship(
        back_populates="well_model", uselist=False
    )
    well_day_plan_model: Mapped["WellDayPlanModel"] = relationship(
        back_populates="well_model", uselist=False
    )
