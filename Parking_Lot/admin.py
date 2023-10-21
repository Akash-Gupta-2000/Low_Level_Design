class Admin:
    def add_floor_to_lot(self, parking_lot, floor):
        parking_lot.add_floor(floor)

    def add_parking_slot_to_floor(self, floor, slot):
        floor.add_parking_slot(slot)

    def remove_parking_slot_from_floor(self, floor, slot):
        floor.remove_parking_slot(slot)

    def add_entry_panel_to_lot(self, parking_lot, entry_panel):
        parking_lot.add_entry_panel(entry_panel)

    def add_exit_panel_to_lot(self, parking_lot, exit_panel):
        parking_lot.add_exit_panel(exit_panel)
