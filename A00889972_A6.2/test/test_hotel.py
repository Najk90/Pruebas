"""
Unit tests for the Hotel class.

Author: Najk
Date: 16-02-2024.
"""

import unittest
from src.file_manager import FileManager


class TestHotelMethods(unittest.TestCase):
    """Test class for the Hotel methods."""

    def setUp(self):
        """Set up the test environment."""
        self.file_manager = FileManager()

    def test_create_hotel(self):
        """Test creating a new hotel."""
        FileManager.save_to_file([], "data/test_hotels.json")

        self.file_manager.create_hotel(
            "Hotel Test",
            "Test Location",
            ["101", "102"],
            "data/test_hotels.json"
        )
        hotels_data = self.file_manager.load_from_file(
            "data/test_hotels.json"
        )

        self.assertIsNotNone(hotels_data)
        self.assertEqual(len(hotels_data), 1)
        self.assertEqual(hotels_data[0]['name'], "Hotel Test")

    def test_delete_hotel(self):
        """Test deleting a hotel."""
        self.file_manager.create_hotel(
            "Hotel Test",
            "Test Location",
            ["101", "102"],
            "data/test_hotels.json"
        )
        self.file_manager.delete_hotel_from_file(
            "Hotel Test",
            "data/test_hotels.json"
        )
        hotels_data = self.file_manager.load_from_file(
            "data/test_hotels.json"
        )
        self.assertIsNotNone(hotels_data)
        self.assertEqual(len(hotels_data), 0)

    def test_modify_hotel_info(self):
        """Test modifying hotel information."""
        self.file_manager.create_hotel(
            "Hotel Test",
            "Test Location",
            ["101", "102"],
            "data/test_hotels.json"
        )
        updated_info = {
            'name': 'Hotel Test',
            'location': 'New Location',
            'rooms': ['201', '202']
        }
        self.file_manager.modify_hotel_info_in_file(
            updated_info,
            "data/test_hotels.json"
        )
        hotels_data = self.file_manager.load_from_file(
            "data/test_hotels.json"
        )
        self.assertIsNotNone(hotels_data)
        self.assertEqual(
            hotels_data[0]['location'],
            'New Location'
        )

    def test_invalid_hotel_file(self):
        """Test handling invalid hotel file."""
        hotels_data = self.file_manager.load_from_file(
            "file_doesnt_exist.json"
        )
        self.assertIsNone(hotels_data)


if __name__ == "__main__":
    unittest.main()
