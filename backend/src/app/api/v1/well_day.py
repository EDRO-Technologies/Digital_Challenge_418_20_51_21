from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.schemas.well_day import DebitPerMonthSchema, MostEESchema, MostPerfomanceSchema
from app.depends import get_current_user
from app.dto.user import DatabaseUser
from app.ports.uow import UoW
from app.services.well_day import WellDayService, WeekEnergyConsumption

router = APIRouter(prefix="/well_day")


@router.get(
    "/debit/last_mont", response_model=DebitPerMonthSchema, status_code=200
)
async def get_last_mont_debit(
    uow: Annotated[UoW, Depends()],
    service: Annotated[WellDayService, Depends()],
    user: DatabaseUser = Depends(get_current_user),
) -> DebitPerMonthSchema:
    return await service.get_last_month_debit(uow)


@router.get(
    "/most_ee_wells", response_model=MostEESchema, status_code=200
)
async def get_most_ee_wells(
    uow: Annotated[UoW, Depends()],
    service: Annotated[WellDayService, Depends()],
    user: DatabaseUser = Depends(get_current_user),
):
    return await service.get_most_ee_wells(uow)


@router.get(
    "/most_perfomance", response_model=MostPerfomanceSchema, status_code=200
)
async def get_most_perfomance(
    uow: Annotated[UoW, Depends()],
    service: Annotated[WellDayService, Depends()],
    user: DatabaseUser = Depends(get_current_user),
) -> MostPerfomanceSchema:
    return await service.get_most_perfomance_wells(uow)


@router.get(
    "/energy_consumption", response_model=WeekEnergyConsumption, status_code=200
)
async def get_energy_consumption(
    uow: Annotated[UoW, Depends()],
    service: Annotated[WellDayService, Depends()],
    user: DatabaseUser = Depends(get_current_user),
):
    return await service.get_energy_consumption(uow)
