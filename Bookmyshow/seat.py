class Seat:
    def __init__(self, seat_type):
        self.seat_type = seat_type
        self.is_booked = False

    def book(self):
        self.is_booked = True
