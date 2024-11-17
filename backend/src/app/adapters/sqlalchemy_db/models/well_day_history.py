from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import DATE, FLOAT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.sqlalchemy_db.models.base import Base

if TYPE_CHECKING:
    from app.adapters.sqlalchemy_db.models.well import WellModel


class WellDayHistoryModel(Base):
    __tablename__ = "well_day_histories"

    well: Mapped[int] = mapped_column(
        ForeignKey("wells.well", ondelete="CASCADE"),
        primary_key=True,
    )
    date_fact: Mapped[date] = mapped_column(DATE, primary_key=True)
    debit: Mapped[float] = mapped_column(FLOAT)
    ee_consume: Mapped[float] = mapped_column(FLOAT)
    expenses: Mapped[float] = mapped_column(FLOAT)
    pump_operating: Mapped[float] = mapped_column(FLOAT)

    well_model: Mapped["WellModel"] = relationship(
        back_populates="well_day_history_model", uselist=False
    )
