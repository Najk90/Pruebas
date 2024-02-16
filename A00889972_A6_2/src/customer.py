"""
Customer Module
This module contains the Customer class representing a customer entity.
"""


class Customer:
    """
    Represents a customer.

    Attributes:
        name (str): The name of the customer.
        email (str): The email of the customer.
        phone (str): The phone number of the customer.
    """

    def __init__(self, name, email, phone):
        """
        Initialize a Customer instance.

        Args:
            name (str): The name of the customer.
            email (str): The email of the customer.
            phone (str): The phone number of the customer.
        """
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        """
        Convert the customer to a dictionary.

        Returns:
            dict: A dictionary representation of the customer.
        """
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Customer instance from a dictionary.

        Args:
            data (dict): The dictionary containing customer data.

        Returns:
            Customer: A Customer instance created from the dictionary data.
        """
        return cls(data['name'], data['email'], data['phone'])

    def display_info(self):
        """
        Display information about the customer.
        """
        print(f"Customer Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")

    def modify_info(self, name=None, email=None, phone=None):
        """
        Modify the customer's information.

        Args:
            name (str, optional): The new name of the customer.
            email (str, optional): The new email of the customer.
            phone (str, optional): The new phone number of the customer.
        """
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        print("Customer information updated successfully.")
