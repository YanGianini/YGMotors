from app.infra.database.orm_base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime


class SaleORM(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    buyer_cpf = Column(String(14), nullable=False)
    sale_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)