from datetime import datetime
from dataclasses import dataclass

@dataclass
class Sale:
    id: int | None
    vehicle_id: int
    buyer_cpf: str
    sale_date: datetime
    created_at: datetime
    updated_at: datetime


    @staticmethod
    def create(vehicle_id: int, buyer_cpf: str) -> "Sale":
        return Sale(
            id=None,
            vehicle_id=vehicle_id,
            buyer_cpf=buyer_cpf,
            date=datetime.utcnow()
        )
    
