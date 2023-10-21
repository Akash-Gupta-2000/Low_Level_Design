from enum import Enum

class VehicleType(Enum):
    ACTIVA = "Activa"
    POLO = "Polo"
    XUV = "XUV"

class SelectionStrategy(Enum):
    PREFERRED_VEHICLE = "Preferred Vehicle"
    MOST_VACANT = "Most Vacant"
