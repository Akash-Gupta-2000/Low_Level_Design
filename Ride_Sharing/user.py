class User:
    def __init__(self, user_id, user_details):
        self.user_id = user_id
        self.user_details = user_details
        self.vehicles = []
        self.offered_rides = []
        self.taken_rides = []

    def add_vehicle(self, vehicle_details):
        self.vehicles.append(vehicle_details)

    def offer_ride(self, ride_details):
        ride = Ride(ride_details, self)
        self.offered_rides.append(ride)

    def select_ride(self, source, destination, seats, selection_strategy):
        # Implement the selection strategy logic here
        # For example, choose the ride based on the strategy
        selected_ride = ""
        return selected_ride

    def end_ride(self, ride_details):
        # End the specified ride
        pass

class Driver(User):
    def offer_ride(self, ride_details):
        ride = Ride(ride_details, self)
        self.offered_rides.append(ride)

class Passenger(User):
    def select_ride(self, source, destination, seats, selection_strategy):
        selected_ride = super().select_ride(source, destination, seats, selection_strategy)
        if selected_ride:
            selected_ride.add_passenger(self)
            return selected_ride

class Ride:
    def __init__(self, ride_details, driver):
        self.ride_details = ride_details
        self.driver = driver
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
