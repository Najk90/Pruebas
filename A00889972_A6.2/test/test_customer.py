"""
Unit tests for customer-related actions.

Author: Najk
Date: 16-02-2024.
"""

import unittest
from src.file_manager import FileManager


class TestCustomerMethods(unittest.TestCase):
    """Test class for customer-related actions."""

    def setUp(self):
        """Set up the test environment."""
        self.file_manager = FileManager()

    def test_create_customer(self):
        """Test creating a new customer."""
        FileManager.save_to_file([], "data/test_customers.json")

        self.file_manager.create_customer(
            "John Doe",
            "john@example.com",
            "123-456-7890",
            "data/test_customers.json"
        )
        customers_data = self.file_manager.load_from_file(
            "data/test_customers.json"
        )

        self.assertIsNotNone(customers_data)
        self.assertEqual(len(customers_data), 1)
        self.assertEqual(customers_data[0]['name'], "John Doe")

    def test_delete_customer(self):
        """Test deleting a customer."""
        self.file_manager.create_customer(
            "John Doe",
            "john@example.com",
            "123-456-7890",
            "data/test_customers.json"
        )
        self.file_manager.delete_customer_from_file(
            "John Doe", "data/test_customers.json"
        )
        customers_data = self.file_manager.load_from_file(
            "data/test_customers.json"
        )
        self.assertIsNotNone(customers_data)
        self.assertEqual(len(customers_data), 0)

    def test_modify_customer_info(self):
        """Test modifying customer information."""
        self.file_manager.create_customer(
            "John Doe",
            "john@example.com",
            "123-456-7890",
            "data/test_customers.json"
        )
        updated_info = {
            'name': 'John Doe', 'email':
            'john_modified@example.com',
            'phone': '999-999-9999'
        }
        self.file_manager.modify_customer_info_in_file(
            updated_info, "data/test_customers.json"
        )
        customers_data = self.file_manager.load_from_file(
            "data/test_customers.json"
        )
        self.assertIsNotNone(customers_data)
        self.assertEqual(
            customers_data[0]['email'],
            'john_modified@example.com'
        )

    def test_invalid_customer_file(self):
        """Test handling an invalid customer file."""
        customers_data = self.file_manager.load_from_file(
            "file_doesnt_exist.json"
        )
        self.assertIsNone(customers_data)


if __name__ == "__main__":
    unittest.main()
