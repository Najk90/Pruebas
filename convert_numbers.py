"""

Converts numbers from a file into binary and hexadecimal representation.

This script reads numbers from a file, converts them to binary and hexadecimal,
and saves the results in a text file named ConversionResults.txt.

Usage: python convert_numbers.py fileWithData.txt

Author: Najk
Date: 01-02-2024.
"""

import sys
import time


def read_file(file_name):
    """
    Read numbers from a file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A list of numbers read from the file.
    """
    numbers = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    if number.is_integer():
                        numbers.append(int(number))
                    else:
                        numbers.append(number)
                except ValueError:
                    print(f"Invalid data: '{line.strip()}'")
    except FileNotFoundError:
        print("File not found.")
    return numbers


def convert_to_binary(number):
    """
    Convert a number to binary.

    Args:
        number (float): The number to convert.

    Returns:
        str: The binary representation of the number.
    """
    if number < 0:
        return "-" + convert_to_binary(-number)
    integer_part = int(number)
    fractional_part = number - integer_part
    integer_binary = bin(integer_part)[2:]
    if fractional_part == 0:
        return integer_binary
    fractional_binary = ""
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary += str(bit)
        fractional_part -= bit
    return integer_binary + "." + fractional_binary.rstrip('0')


def convert_to_hexadecimal(number):
    """
    Convert a number to hexadecimal.

    Args:
        number (float): The number to convert.

    Returns:
        str: The hexadecimal representation of the number.
    """
    if number < 0:
        return "-" + convert_to_hexadecimal(-number)
    integer_part = int(number)
    fractional_part = number - integer_part
    integer_hex = hex(integer_part)[2:]
    if fractional_part == 0:
        return integer_hex
    fractional_hex = ""
    while fractional_part:
        fractional_part *= 16
        digit = int(fractional_part)
        if digit < 10:
            fractional_hex += str(digit)
        else:
            fractional_hex += chr(ord('A') + digit - 10)
        fractional_part -= digit
    return integer_hex + "." + fractional_hex.rstrip('0')


def process_file(file_name):
    """
    Process a file to convert numbers to binary and hexadecimal.

    Args:
        file_name (str): The name of the file to process.
    """
    numbers = read_file(file_name)
    binary_results = [
        convert_to_binary(number) for number in numbers]
    hexadecimal_results = [
        convert_to_hexadecimal(number) for number in numbers]

    with open("ConversionResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write("Conversion Results:\n")
        result_file.write(
            "NUMBER\t"+file_name.strip('.txt')+"\tBIN\t\t\t\tHEX\n")

        print("Conversion Results:")
        print("NUMBER\t"+file_name.strip('.txt')+"\tBIN\t\t\t\tHEX")
        for i, (number, binary, hexadecimal) in enumerate(
                zip(numbers, binary_results, hexadecimal_results)):
            print(f"{i + 1}\t{number}\t{binary}\t\t{hexadecimal}")
            result_file.write(
                f"{i + 1}\t{number}\t{binary}\t\t{hexadecimal}\n")


def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py fileWithData.txt")
        return

    file_name = sys.argv[1]

    start_time = time.time()

    process_file(file_name)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Time elapsed: {elapsed_time} seconds")

    with open("ConversionResults.txt", 'a', encoding='utf-8') as result_file:
        result_file.write(f"Time elapsed: {elapsed_time} seconds\n")

if __name__ == "__main__":
    main()
