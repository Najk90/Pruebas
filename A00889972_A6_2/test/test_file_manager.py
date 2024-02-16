"""Unit tests for the FileManager class."""

import unittest
from src.file_manager import FileManager
from src.hotel import Hotel


class TestFileManagerMethods(unittest.TestCase):
    """Test class for the FileManager methods."""

    def setUp(self):
        """Set up the test environment."""
        self.file_manager = FileManager()

    def test_save_and_load_to_file(self):
        """Test saving and loading data to/from file."""
        data = [{
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123-456-7890'
        }]
        self.file_manager.save_to_file(data, "data/test_data.json")
        loaded_data = self.file_manager.load_from_file("data/test_data.json")
        self.assertIsNotNone(loaded_data)
        self.assertEqual(len(loaded_data), 1)
        self.assertEqual(loaded_data[0]['name'], "John Doe")

    def test_save_and_load_hotel_to_file(self):
        """Test saving and loading hotel data to/from file."""
        FileManager.save_to_file([], "data/test_hotels.json")

        hotel = Hotel("Hotel Test", "Test Location", ["101", "102"])
        self.file_manager.save_hotel_to_file(hotel, "data/test_hotels.json")
        hotels_data = self.file_manager.load_from_file("data/test_hotels.json")

        self.assertIsNotNone(hotels_data)
        self.assertEqual(len(hotels_data), 1)
        self.assertEqual(hotels_data[0]['name'], "Hotel Test")


if __name__ == "__main__":
    unittest.main()
