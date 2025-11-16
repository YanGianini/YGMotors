from sqlalchemy import (
    Table, Column, String, Integer, Float, DateTime, MetaData
)
from datetime import datetime
from app.domain.models.vehicle_status import VehicleStatusEnum


metadata = MetaData()

vehicle_table = Table(
    "vehicles",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("brand", String(100), nullable=False),
    Column("model", String(100), nullable=False),
    Column("year", Integer, nullable=False),
    Column("color", String(50), nullable=False),
    Column("price", Float, nullable=False),
    Column("status", String(20), nullable=False, default=VehicleStatusEnum.AVAILABLE.value),
    Column("created_at", DateTime(timezone=True), nullable=False, default=datetime.utcnow),
    Column("updated_at", DateTime(timezone=True), nullable=False, default=datetime.utcnow),
)
