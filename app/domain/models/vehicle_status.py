from enum import Enum


class VehicleStatusEnum(str, Enum):
    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"
    SOLD = "Sold"
