"""
Hotel Module
This module contains the Hotel class representing a hotel entity.
"""


class Hotel:
    """
    Represents a hotel.

    Attributes:
        name (str): The name of the hotel.
        location (str): The location of the hotel.
        rooms (list): The list of available rooms in the hotel.
    """

    def __init__(self, name, location, rooms):
        """
        Initialize a Hotel instance.

        Args:
            name (str): The name of the hotel.
            location (str): The location of the hotel.
            rooms (list): The list of available rooms in the hotel.
        """
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """
        Convert the hotel to a dictionary.

        Returns:
            dict: A dictionary representation of the hotel.
        """
        return {
            'name': self.name,
            'location': self.location,
            'rooms': self.rooms
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Hotel instance from a dictionary.

        Args:
            data (dict): The dictionary containing hotel data.

        Returns:
            Hotel: A Hotel instance created from the dictionary data.
        """
        return cls(data['name'], data['location'], data['rooms'])

    def reserve_room(self, room_number):
        """
        Reserve a room in the hotel.

        Args:
            room_number (str): The room number to be reserved.
        """
        if room_number in self.rooms:
            print(f"Room {room_number} reserved successfully.")
        else:
            print(f"Room {room_number} is not available.")

    def cancel_reservation(self, room_number):
        """
        Cancel a reservation for a room in the hotel.

        Args:
            room_number (str):
                The room number for which the reservation should be canceled.
        """
        if room_number in self.rooms:
            print(f"Reservation for room {room_number} canceled successfully.")
        else:
            print(f"No reservation found for room {room_number}.")

    def display_info(self):
        """
        Display information about the hotel.
        """
        print(f"Hotel Name: {self.name}")
        print(f"Location: {self.location}")
        print("Rooms:")
        for room in self.rooms:
            print(f"- Room {room}")

    def modify_info(self, name=None, location=None, rooms=None):
        """
        Modify the hotel's information.

        Args:
            name (str, optional):
                The new name of the hotel.
            location (str, optional):
                The new location of the hotel.
            rooms (list, optional):
                The new list of available rooms in the hotel.
        """
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms:
            self.rooms = rooms
        print("Hotel information updated successfully.")
