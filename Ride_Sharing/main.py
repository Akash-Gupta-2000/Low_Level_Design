from enums import VehicleType, SelectionStrategy
from ride_sharing_system import RideSharingSystem

if __name__ == "__main__":
    ride_sharing_system = RideSharingSystem()

    # Add users
    user1_details = {"name": "Alice", "phone": "123-456-7890"}
    ride_sharing_system.add_user(user1_details)

    user2_details = {"name": "Bob", "phone": "987-654-3210"}
    ride_sharing_system.add_user(user2_details)

    # Add vehicles for users
    vehicle1_details = {"type": VehicleType.ACTIVA, "plate_number": "AB1234"}
    ride_sharing_system.users[0].add_vehicle(vehicle1_details)

    # Offer rides
    ride1_details = {"vehicle": ride_sharing_system.users[0].vehicles[0], "origin": "A", "destination": "B", "available_seats": 3}
    ride_sharing_system.users[0].offer_ride(ride1_details)

    # Select rides
    selected_ride = ride_sharing_system.users[1].select_ride("A", "B", 2, SelectionStrategy.MOST_VACANT)

    # End rides
    ride_sharing_system.end_ride(selected_ride)

    # Print ride statistics
    ride_sharing_system.print_ride_stats()
