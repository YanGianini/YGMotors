from dataclasses import dataclass
from datetime import datetime

from app.domain.models.vehicle_status import VehicleStatusEnum


@dataclass
class Vehicle:
    id: int | None
    brand: str
    model: str
    year: int
    color: str
    price: float
    status: VehicleStatusEnum
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(brand: str, model: str, year: int, color: str, price: float) -> "Vehicle":
        now = datetime.utcnow()
        return Vehicle(
            id=None,
            brand=brand,
            model=model,
            year=year,
            color=color,
            price=price,
            status=VehicleStatusEnum.AVAILABLE,
            created_at=now,
            updated_at=now,
        )
