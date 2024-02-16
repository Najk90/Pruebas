"""
Reservation Module
This module contains the Reservation class representing a hotel reservation.
"""

from src.customer import Customer
from src.hotel import Hotel


class Reservation:
    """
    Represents a hotel reservation.

    Attributes:
        customer (Customer): The customer making the reservation.
        hotel (Hotel): The hotel where the reservation is made.
        room_number (str): The room number for the reservation.
    """

    def __init__(self, customer, hotel, room_number):
        """
        Initialize a Reservation instance.

        Args:
            customer (Customer): The customer making the reservation.
            hotel (Hotel): The hotel where the reservation is made.
            room_number (str): The room number for the reservation.
        """
        self.customer = customer
        self.hotel = hotel
        self.room_number = room_number

    def to_dict(self):
        """
        Convert the reservation to a dictionary.

        Returns:
            dict: A dictionary representation of the reservation.
        """
        return {
            'customer': self.customer.to_dict(),
            'hotel': self.hotel.to_dict(),
            'room_number': self.room_number
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Reservation instance from a dictionary.

        Args:
            data (dict): The dictionary containing reservation data.

        Returns:
            Reservation:
                A Reservation instance created from the dictionary data.
        """
        customer = Customer.from_dict(data['customer'])
        hotel = Hotel.from_dict(data['hotel'])
        return cls(customer, hotel, data['room_number'])

    def cancel_reservation(self):
        """
        Cancel the reservation and print a confirmation message.
        """
        print(f"Reservation for {self.customer.name} at {self.hotel.name}, "
              f"Room {self.room_number} canceled successfully.")
