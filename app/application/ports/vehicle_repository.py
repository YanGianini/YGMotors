from abc import ABC, abstractmethod
from app.domain.models.vehicle import Vehicle


class VehicleRepository(ABC):

    @abstractmethod
    async def create(self, vehicle: Vehicle) -> Vehicle:
        pass

    @abstractmethod
    async def get_by_id(self, vehicle_id: int) -> Vehicle | None:
        pass
