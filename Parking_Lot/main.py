from enums import ParkingSlotType
from parking_slot import ParkingSlot
from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from admin import Admin
from payment import Payment
import datetime

# Create parking slots
slot1 = ParkingSlot(1, ParkingSlotType.CAR)
slot2 = ParkingSlot(2, ParkingSlotType.CAR)
slot3 = ParkingSlot(3, ParkingSlotType.MOTORBIKE)
slot4 = ParkingSlot(4, ParkingSlotType.MOTORBIKE)

# Create parking floor and add slots
floor1 = ParkingFloor(1)
floor1.add_parking_slot(slot1)
floor1.add_parking_slot(slot2)
floor1.add_parking_slot(slot3)
floor1.add_parking_slot(slot4)

# Create parking lot and add a floor
parking_lot = ParkingLot()
parking_lot.add_floor(floor1)

# Create admin
admin = Admin()

# Add an entrance panel and an exit panel to the parking lot
entry_panel = "Entrance Panel 1"
exit_panel = "Exit Panel 1"
admin.add_entry_panel_to_lot(parking_lot, entry_panel)
admin.add_exit_panel_to_lot(parking_lot, exit_panel)

# Simulate issuing a ticket
ticket = parking_lot.issue_ticket(entry_panel, ParkingSlotType.CAR)

# Define entry and exit times
entry_time = datetime.datetime(2023, 10, 21, 8, 0, 0)
exit_time = datetime.datetime(2023, 10, 21, 15, 30, 0)

# Simulate paying for the ticket
payment = Payment()
charge = payment.calculate_charges(entry_time, exit_time, ParkingSlotType.CAR)
if parking_lot.pay_for_ticket(exit_panel, ticket):
    print("Payment successful. Vehicle can exit the parking lot.")
else:
    print("Payment failed. Vehicle cannot exit the parking lot.")
