"""
Compute Sales

This script computes the total cost of sales
based on a price catalogue and sales records.

Usage:
python compute_sales.py Catalogue.json sales.json

Author: Najk
Date: 01-02-2024.
"""

import json
import sys
import time


def load_json_file(file_path):
    """
    Load JSON data from a file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data.

    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {file_path}: {e}")
        return None


def compute_total_cost(price_catalogue, sales_record):
    """
    Compute the total cost of sales.

    Args:
        price_catalogue (dict): The catalogue of prices.
        sales_record (list): The list of sales records.

    Returns:
        float: The total cost of sales.

    """
    total_cost = 0
    for sale in sales_record:
        product_name = sale.get('Product')
        if product_name:
            item_price = next(
                (product['price'] for product in price_catalogue
                    if product['title'] == product_name), None)
            if item_price is not None:
                total_cost += sale.get('Quantity', 0) * item_price
            else:
                print(f"Price for product '{product_name}'"
                      " not found in price catalogue.")
        else:
            print("Error: 'Product' key not found in sale record.")
    return round(total_cost, 2)


def main():
    """
    The main function to compute the total cost of sales.

    """
    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py "
              "priceCatalogue.json salesRecord.json")
        return

    start_time = time.time()

    price_catalogue_path = sys.argv[1]
    sales_record_path = sys.argv[2]

    price_catalogue = load_json_file(price_catalogue_path)
    sales_record = load_json_file(sales_record_path)

    if price_catalogue is None or sales_record is None:
        return

    total_cost = compute_total_cost(price_catalogue, sales_record)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Total cost of sales: ${total_cost}")
    print(f"Execution time: {execution_time} seconds")

    with open("SalesResults.txt", "w", encoding='utf-8') as results_file:
        results_file.write(f"Total cost of sales: ${total_cost}\n")
        results_file.write(f"Execution time: {execution_time} seconds\n")


if __name__ == "__main__":
    main()
