from seat import Seat


class Hall:
    def __init__(self, name):
        self.name = name
        self.shows = []
        self.seats = []

    def add_show(self, show):
        self.shows.append(show)

    def add_seats(self, num_seats, seat_type):
        for _ in range(num_seats):
            self.seats.append(Seat(seat_type))
