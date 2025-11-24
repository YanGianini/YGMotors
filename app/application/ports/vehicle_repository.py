from abc import ABC, abstractmethod
from app.domain.models.vehicle import Vehicle


class VehicleRepository(ABC):

    @abstractmethod
    async def create(self, vehicle: Vehicle) -> Vehicle:
        pass

    @abstractmethod
    async def get_by_id(self, vehicle_id: int) -> Vehicle | None:
        pass

    @abstractmethod
    async def update(self, vehicle_id: int, data: dict) -> Vehicle:
        pass

    @abstractmethod
    async def list_by_status(self, status: str) -> list[Vehicle]:
        pass
    