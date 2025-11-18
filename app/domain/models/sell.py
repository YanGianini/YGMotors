from datetime import datetime
from dataclasses import dataclass

@dataclass
class Sell:
    id: int | None
    vehicle_id: int
    buyer_cpf: str
    date: datetime

    @staticmethod
    def create(vehicle_id: int, buyer_cpf: str) -> "Sell":
        return Sell(
            id=None,
            vehicle_id=vehicle_id,
            buyer_cpf=buyer_cpf,
            date=datetime.utcnow()
        )
    
