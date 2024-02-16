"""
Unit tests for actions performed by the FileManager class.

Author: Najk
Date: 16-02-2024.
"""

import unittest
from src.file_manager import FileManager
from src.customer import Customer
from src.hotel import Hotel
from src.reservation import Reservation


class TestFileManagerActions(unittest.TestCase):
    """Test class for actions performed by the FileManager class."""

    def setUp(self):
        """Set up the test environment."""
        self.file_manager = FileManager()
        self.initial_customers_data = self.remove_duplicates(
            self.file_manager.load_from_file("data/test_customers.json"))
        self.initial_reservations_data = self.remove_duplicates(
            self.file_manager.load_from_file("data/test_reservations.json"))
        self.initial_hotels_data = self.remove_duplicates(
            self.file_manager.load_from_file("data/test_hotels.json"))

    def remove_duplicates(self, data):
        """Remove duplicates from the data."""
        unique_data = []
        for item in data:
            if item not in unique_data:
                unique_data.append(item)
        return unique_data

    def test_create_existing_customer(self):
        """Test creating a customer that already exists."""
        customer = Customer(
            "John Doe", "john@example.com", "123-456-7890")
        self.file_manager.save_customer_to_file(
            customer, "data/test_customers.json")
        self.file_manager.save_customer_to_file(
            customer, "data/test_customers.json")
        customers_data = self.remove_duplicates(
            self.file_manager.load_from_file("data/test_customers.json"))
        self.assertEqual(
            len(customers_data),
            len(self.initial_customers_data) + 1
        )

    def test_create_existing_hotel(self):
        """Test creating a hotel that already exists."""
        hotel = Hotel("Hotel Test", "Test Location", ["101", "102"])
        self.file_manager.save_hotel_to_file(
            hotel, "data/test_hotels.json")
        self.file_manager.save_hotel_to_file(
            hotel, "data/test_hotels.json")
        hotels_data = self.file_manager.load_from_file("data/test_hotels.json")
        self.assertEqual(len(hotels_data), len(self.initial_hotels_data))

    def test_create_existing_reservation(self):
        """Test creating a reservation that already exists."""
        customer = Customer("John Doe", "john@example.com", "123-456-7890")
        hotel = Hotel("Hotel A", "City A", ["101", "102"])
        reservation = Reservation(customer, hotel, "101")
        self.file_manager.save_reservation_to_file(
            reservation, "data/test_reservations.json")
        self.file_manager.save_reservation_to_file(
            reservation, "data/test_reservations.json")
        reservations_data = self.remove_duplicates(
            self.file_manager.load_from_file("data/test_reservations.json"))
        self.assertEqual(
            len(reservations_data), len(self.initial_reservations_data))


if __name__ == "__main__":
    unittest.main()
