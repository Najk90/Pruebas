"""
FileManager Module
This module provides functionality for saving and loading data to/from files.

Author: Najk
Date: 16-02-2024.
"""

import json
import os
from src.hotel import Hotel
from src.customer import Customer


class FileManager:
    """
        FileManager class provides methods
        for saving and loading data to/from files.
    """

    @staticmethod
    def save_to_file(data, filename):
        """
        Save data to a file.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    @staticmethod
    def load_from_file(filename):
        """
        Load data from a file.
        Returns:
            list: The loaded data.
        """
        if not os.path.exists(filename):
            return None
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            unique_data = []
            for item in data:
                if item not in unique_data:
                    unique_data.append(item)
            return unique_data

    # Start of the Hotel Section.

    @staticmethod
    def save_hotel_to_file(hotel, filename):
        """Save hotel data to a file."""
        hotels_data = FileManager.load_from_file(filename)
        if hotels_data is None:
            hotels_data = []
        for existing_hotel in hotels_data:
            if existing_hotel['name'] == hotel.name:
                print(f"Hotel with name {hotel.name} already exists.")
                return
        hotels_data.append(hotel.to_dict())
        FileManager.save_to_file(hotels_data, filename)

    @staticmethod
    def delete_hotel_from_file(hotel_name, filename):
        """Delete a hotel from the file."""
        hotels_data = FileManager.load_from_file(filename)
        if hotels_data is not None:
            updated_hotels_data = [
                hotel for hotel in hotels_data
                if hotel['name'] != hotel_name]
            FileManager.save_to_file(updated_hotels_data, filename)

    @staticmethod
    def display_hotels_from_file(filename):
        """Display hotels from the file."""
        hotels_data = FileManager.load_from_file(filename)
        if hotels_data is not None:
            for hotel in hotels_data:
                print(hotel)

    @staticmethod
    def modify_hotel_info_in_file(updated_hotel_data, filename):
        """Modify hotel information in the file."""
        hotels_data = FileManager.load_from_file(filename)
        if hotels_data is not None:
            for hotel in hotels_data:
                if hotel['name'] == updated_hotel_data['name']:
                    hotel.update(updated_hotel_data)
                    break
            FileManager.save_to_file(hotels_data, filename)

    @staticmethod
    def create_hotel(name, location, rooms, filename):
        """Create a new hotel and save it to the file."""
        hotel = Hotel(name, location, rooms)
        FileManager.save_hotel_to_file(hotel, filename)

    # Start of the Costumer Section.

    @staticmethod
    def save_customer_to_file(customer, filename):
        """Save customer data to a file."""
        customers_data = FileManager.load_from_file(filename)
        if customers_data is None:
            customers_data = []
        for existing_customer in customers_data:
            if existing_customer['email'] == customer.email:
                print(f"Customer with email {customer.email} already exists.")
                return
        customers_data.append(customer.to_dict())
        FileManager.save_to_file(customers_data, filename)

    @staticmethod
    def delete_customer_from_file(customer_name, filename):
        """Delete a customer from the file."""
        customers_data = FileManager.load_from_file(filename)
        if customers_data is not None:
            updated_customers_data = [
                customer for customer in customers_data
                if customer['name'] != customer_name]
            FileManager.save_to_file(updated_customers_data, filename)

    @staticmethod
    def display_customers_from_file(filename):
        """Display customers from the file."""
        customers_data = FileManager.load_from_file(filename)
        if customers_data is not None:
            for customer in customers_data:
                print(customer)

    @staticmethod
    def modify_customer_info_in_file(updated_customer_data, filename):
        """Modify customer information in the file."""
        customers_data = FileManager.load_from_file(filename)
        if customers_data is not None:
            for customer in customers_data:
                if customer['name'] == updated_customer_data['name']:
                    customer.update(updated_customer_data)
                    break
            FileManager.save_to_file(customers_data, filename)

    @staticmethod
    def create_customer(name, email, phone, filename):
        """Create a new customer and save it to the file."""
        customer = Customer(name, email, phone)
        FileManager.save_customer_to_file(customer, filename)

    # Start of the Reservations Section.

    @staticmethod
    def save_reservation_to_file(reservation, filename):
        """Save reservation data to a file."""
        reservations_data = FileManager.load_from_file(filename)
        if reservations_data is None:
            reservations_data = []
        for r in reservations_data:
            if (
                r['customer']['email'] == reservation.customer.email and
                r['hotel']['name'] == reservation.hotel.name and
                r['room_number'] == reservation.room_number
            ):
                print("Reservation already exists.")
                return
        reservations_data.append(reservation.to_dict())
        FileManager.save_to_file(reservations_data, filename)

    @staticmethod
    def cancel_reservation_from_file(
            customer_name, hotel_name, room_number, filename):
        """Cancel a reservation from the file."""
        reservations_data = FileManager.load_from_file(filename)
        if reservations_data is not None:
            updated_reservations_data = [
                reservation for reservation in reservations_data
                if any([
                    reservation['customer']['name'] != customer_name,
                    reservation['hotel']['name'] != hotel_name,
                    reservation['room_number'] != room_number
                ])
            ]
            FileManager.save_to_file(updated_reservations_data, filename)
