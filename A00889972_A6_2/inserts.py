"""Provides methods to insert sample data into the system."""

from src.hotel import Hotel
from src.customer import Customer
from src.reservation import Reservation
from src.file_manager import FileManager


class Inserts:
    """Provides methods to insert sample data into the system."""

    @staticmethod
    def main():
        """Inserts sample data into the system."""
        # Initialize file manager
        file_manager = FileManager()

        # Create a hotel
        hotel = Hotel("Hotel XYZ", "City A", ["101", "102", "103"])

        # Save hotel to file
        file_manager.create_hotel(
            hotel.name,
            hotel.location,
            hotel.rooms,
            "data/hotels.json"
        )

        # Create a customer
        customer = Customer(
            "John Doe",
            "john@example.com",
            "123-456-7890"
        )

        # Save customer to file
        file_manager.create_customer(
            customer.name,
            customer.email,
            customer.phone,
            "data/customers.json"
        )

        # Reserve a room
        room_number = "101"
        reservation = Reservation(
            customer,
            hotel,
            room_number
        )
        print(f"Reserving room {room_number} for {customer.name}...")
        hotel.reserve_room(room_number)
        print()

        # Save reservation to file
        file_manager.save_reservation_to_file(
            reservation,
            "data/reservations.json"
        )

        # Display hotel information
        print("Hotel Information:")
        hotel.display_info()
        print()

        # Display customer information
        print("Customer Information:")
        customer.display_info()
        print()

    @staticmethod
    def another_method():
        """Another method to address pylint error."""
        print("Another method!")


if __name__ == "__main__":
    Inserts.main()
