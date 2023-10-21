from enum import Enum

class PaymentType(Enum):
    CREDIT_CARD = "Credit Card"
    CASH = "Cash"

class SeatType(Enum):
    NORMAL = "Normal"
    VIP = "VIP"
