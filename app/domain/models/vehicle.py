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

    @classmethod
    def from_orm(cls, orm_obj):
        return cls(
            id=orm_obj.id,
            brand=orm_obj.brand,
            model=orm_obj.model,
            year=orm_obj.year,
            color=orm_obj.color,
            price=orm_obj.price,
            status=orm_obj.status,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at
        )

