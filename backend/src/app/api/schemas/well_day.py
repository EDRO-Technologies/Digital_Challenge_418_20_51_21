from datetime import date

from pydantic import BaseModel


class DayDebitSchema(BaseModel):
    name: str
    presence: int
    plan: int


class DebitPerMonthSchema(BaseModel):
    days: list[DayDebitSchema]


class MostEESchema(BaseModel):
    well_names: list[str]


# class DebitPerMonthSchema(BaseModel):
#     days: list[DayDebitSchema]


class MostPerfomanceSchema(BaseModel):
    well_names: list[str]


class DayEnergyConsumption(BaseModel):
    name: str
    value: float


class WeekEnergyConsumption(BaseModel):
    days: list[DayEnergyConsumption]
