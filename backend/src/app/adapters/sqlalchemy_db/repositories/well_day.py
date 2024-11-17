import datetime
from typing import Sequence

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.sqlalchemy_db.models.object import ObjectModel
from app.adapters.sqlalchemy_db.models.well_day_plan import WellDayPlanModel
from app.adapters.sqlalchemy_db.models.well_day_history import WellDayHistoryModel
from app.api.schemas.well_day import DayEnergyConsumption, WeekEnergyConsumption
from app.ports.repositories.well_day import WellDayRepository


class SqlalWellDayRepository(WellDayRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_last_month_debit_plan(
        self, start_day: datetime.date, finish_day: datetime.date
    ):
        query = (
            select(
                WellDayPlanModel.date_plan,
                func.sum(WellDayPlanModel.debit).label("total_debit"),
            )
            .where(
                WellDayPlanModel.date_plan >= start_day,
                WellDayPlanModel.date_plan <= finish_day,
            )
            .group_by(WellDayPlanModel.date_plan)
            .order_by(WellDayPlanModel.date_plan)
        )
        result = await self._session.execute(query)
        daily_debit = {row.date_plan: row.total_debit for row in result}

        return daily_debit

    async def get_last_month_debit_history(
        self, start_day: datetime.date, finish_day: datetime.date
    ):
        query = (
            select(
                WellDayHistoryModel.date_fact,
                func.sum(WellDayHistoryModel.debit).label("total_debit"),
            )
            .where(
                WellDayHistoryModel.date_fact >= start_day,
                WellDayHistoryModel.date_fact <= finish_day,
            )
            .group_by(WellDayHistoryModel.date_fact)
            .order_by(
                WellDayHistoryModel.date_fact
            )  # Опционально: сортировка по дате
        )
        result = await self._session.execute(query)

        daily_debit = {row.date_fact: row.total_debit for row in result}
        return daily_debit

    async def get_most_ee_wells(self):
        subquery = (
            select(
                WellDayHistoryModel.well,
                func.sum(WellDayHistoryModel.ee_consume).label('total_energy_consumption')
            )
            .group_by(WellDayHistoryModel.well)
            .subquery()
        )

        main_query = (
            select(
                ObjectModel.id.label('object_id'),
                ObjectModel.name.label('object_name'),
                subquery.c.well,
                subquery.c.total_energy_consumption
            )
            .join(subquery, subquery.c.well == ObjectModel.id)
            .order_by(subquery.c.total_energy_consumption.desc())
            .limit(10)
        )

        top_wells_with_objects = await self._session.execute(main_query)


        return [obj.object_name for obj in top_wells_with_objects.all()]

    async def get_energy_consumption(
        self, start_day: datetime.date,
    ) -> WeekEnergyConsumption:
        query = (
            select(
                WellDayHistoryModel.date_fact,
                func.sum(WellDayHistoryModel.ee_consume).label('total_energy')
            )
            .where(WellDayHistoryModel.date_fact > start_day,
                   WellDayHistoryModel.date_fact <= datetime.datetime.now(datetime.UTC).date())
            .group_by(WellDayHistoryModel.date_fact)
            .order_by(WellDayHistoryModel.date_fact)
        )
        result = await self._session.execute(query)
        result = result.all()
        print(result)
        return WeekEnergyConsumption(
            days=[DayEnergyConsumption(
                name=datetime.datetime.strftime(day[0], "%d.%m"),
                value=round(day[1]),
            ) for day in result]
        )

    async def get_most_perfomance_wells(self) -> Sequence[str]:
        subquery = (
            select(
                WellDayHistoryModel.well,
                func.sum(WellDayHistoryModel.debit).label('total_debit')
            )
            .group_by(WellDayHistoryModel.well)
            .subquery()
        )

        main_query = (
            select(
                ObjectModel.id.label('object_id'),
                ObjectModel.name.label('object_name'),
                subquery.c.well,
                subquery.c.total_debit
            )
            .join(subquery, subquery.c.well == ObjectModel.id)
            .order_by(subquery.c.total_debit.desc())
            .limit(10)
        )

        top_wells_with_objects = await self._session.execute(main_query)


        return [obj.object_name for obj in top_wells_with_objects.all()]
