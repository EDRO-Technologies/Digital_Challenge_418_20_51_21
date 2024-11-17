import datetime
from abc import ABC, abstractmethod
from typing import NoReturn, Sequence


class WellDayRepository(ABC):
    @abstractmethod
    async def get_last_month_debit_plan(
        self, start_day: datetime.date, finish_day: datetime.date
    ) :# -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_last_month_debit_history(
        self, start_day: datetime.date, finish_day: datetime.date
    ):# -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_most_ee_wells(self) -> Sequence[str]:
        raise NotImplementedError

    @abstractmethod
    async def get_energy_consumption(
        self, start_day: datetime.date
    ):
        raise NotImplementedError

    @abstractmethod
    async def get_most_perfomance_wells(self) -> Sequence[str]:
        raise NotImplementedError

