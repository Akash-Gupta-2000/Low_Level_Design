class Booking:
    def __init__(self, customer, seats, payment_type, discount_coupon=None):
        self.customer = customer
        self.seats = seats
        self.payment_type = payment_type
        self.discount_coupon = discount_coupon
