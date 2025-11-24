from sqlalchemy import Column, Integer, String, Float, Enum, DateTime
from datetime import datetime
from app.domain.models.vehicle_status import VehicleStatusEnum
from app.infra.database.orm_base import Base


class VehicleORM(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(Enum(VehicleStatusEnum, name="vehicle_status_enum"), nullable=False, default=VehicleStatusEnum.AVAILABLE)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

