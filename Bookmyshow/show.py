class Show:
    def __init__(self, movie, start_time):
        self.movie = movie
        self.start_time = start_time
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)
