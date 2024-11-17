from datetime import UTC, datetime, timedelta

from app.api.schemas.well_day import DayDebitSchema, DebitPerMonthSchema, MostEESchema, MostPerfomanceSchema, WeekEnergyConsumption
from app.ports.uow import UoW


class WellDayService:
    async def get_last_month_debit(self, uow: UoW) -> DebitPerMonthSchema:
        async with uow:
            start_day = datetime.now(UTC).date() - timedelta(days=30)
            finish_day = datetime.now(UTC).date()
            plan_days = await uow.well_day.get_last_month_debit_plan(
                start_day, finish_day
            )
            history_days = await uow.well_day.get_last_month_debit_history(
                start_day, finish_day
            )
            days = []
            for day_date in plan_days.keys():
                days.append(
                    DayDebitSchema(
                        name=datetime.strftime(day_date, "%d.%m"),
                        presence=history_days[day_date],
                        plan=plan_days[day_date],
                    )
                )
            return DebitPerMonthSchema(days=days)

    async def get_most_ee_wells(self, uow: UoW) -> MostEESchema:
        async with uow:
            well_names = await uow.well_day.get_most_ee_wells()
            return MostEESchema(well_names=well_names)

    async def get_energy_consumption(self, uow: UoW) -> WeekEnergyConsumption:
        async with uow:
            start_day = datetime.now(UTC).date() - timedelta(days=7)
            return await uow.well_day.get_energy_consumption(start_day)

    async def get_most_perfomance_wells(self, uow: UoW) -> MostPerfomanceSchema:
        async with uow:
            well_names = await uow.well_day.get_most_perfomance_wells()
            return MostPerfomanceSchema(well_names=well_names)
