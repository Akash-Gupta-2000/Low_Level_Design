from enums import PaymentType, SeatType
from city import City
from cinema import Cinema
from hall import Hall
from show import Show
from movie import Movie
from customer import Customer
from booking import Booking
from discount_coupon import DiscountCoupon

if __name__ == "__main__":
    # Create a city
    city = City("New York")

    # Create a cinema
    cinema = Cinema("Cineplex")

    # Create a hall
    hall = Hall("Hall 1")

    # Create a movie
    movie = Movie("Avengers: Endgame", "English", "Action", "2019-04-26")

    # Create seats
    hall.add_seats(50, SeatType.NORMAL)
    hall.add_seats(10, SeatType.VIP)

    # Create a show
    show = Show(movie, "2023-04-26 15:00")

    # Book seats
    customer = Customer("John Doe")
    selected_seats = hall.seats[:5]  # Assuming the first 5 seats are selected
    for seat in selected_seats:
        seat.book()
    booking = Booking(customer, selected_seats, PaymentType.CREDIT_CARD)

    # Apply a discount coupon
    discount_coupon = DiscountCoupon("SUMMER20", 20)
    booking.discount_coupon = discount_coupon

    # Add the hall and show to the cinema
    cinema.add_hall(hall)
    hall.add_show(show)

    # Add the cinema to the city
    city.add_cinema(cinema)

    # Display the booked seats and coupon details
    print("Booked seats:")
    for seat in selected_seats:
        print(f"Seat Type: {seat.seat_type}, Booked: {seat.is_booked}")
    print(f"Payment Type: {booking.payment_type}")
    if booking.discount_coupon:
        print(f"Discount Coupon: {booking.discount_coupon.code} ({booking.discount_coupon.discount_percent}%)")
