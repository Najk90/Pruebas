"""
Unit tests for the Reservation class.

Author: Najk
Date: 16-02-2024.
"""

import unittest
from src.customer import Customer
from src.hotel import Hotel
from src.reservation import Reservation
from src.file_manager import FileManager


class TestReservationMethods(unittest.TestCase):
    """Test class for the Reservation methods."""

    def setUp(self):
        """Set up the test environment."""
        self.file_manager = FileManager()

    def test_create_reservation(self):
        """Test creating a new reservation."""
        customer = Customer(
            "John Doe",
            "john@example.com",
            "123-456-7890"
        )
        hotel = Hotel("Hotel A", "City A", ["101", "102"])
        reservation = Reservation(customer, hotel, "101")
        self.file_manager.save_reservation_to_file(
            reservation,
            "data/test_reservations.json"
        )
        reservations_data = self.file_manager.load_from_file(
            "data/test_reservations.json"
        )
        self.assertIsNotNone(reservations_data)
        self.assertEqual(len(reservations_data), 1)
        self.assertEqual(
            reservations_data[0]['customer']['name'],
            "John Doe"
        )

    def test_cancel_reservation(self):
        """Test canceling a reservation."""
        customer = Customer(
            "John Doe",
            "john@example.com",
            "123-456-7890"
        )
        hotel = Hotel("Hotel A", "City A", ["101", "102"])
        reservation = Reservation(customer, hotel, "101")
        self.file_manager.save_reservation_to_file(
            reservation,
            "data/test_reservations.json"
        )
        self.file_manager.cancel_reservation_from_file(
            "John Doe",
            "Hotel A",
            "101",
            "data/test_reservations.json"
        )
        reservations_data = self.file_manager.load_from_file(
            "data/test_reservations.json"
        )
        self.assertIsNotNone(reservations_data)
        self.assertEqual(len(reservations_data), 0)

    def test_invalid_reservation_file(self):
        """Test handling invalid reservation file."""
        reservations_data = self.file_manager.load_from_file(
            "file_doesnt_exist.json"
        )
        self.assertIsNone(reservations_data)


if __name__ == "__main__":
    unittest.main()
