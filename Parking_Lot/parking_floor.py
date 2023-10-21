class ParkingFloor:
    def __init__(self, floor_id):
        self.floor_id = floor_id
        self.slots = []

    def add_parking_slot(self, slot):
        self.slots.append(slot)

    def remove_parking_slot(self, slot):
        self.slots.remove(slot)
