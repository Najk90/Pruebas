"""

Computes descriptive statistics for a list
of numbers provided in a file or directory.

This script reads numbers from a file or
directory, computes descriptive statistics
such as mean, median, mode, variance, and
standard deviation, and saves the results
in a text file named StatisticsResults.txt.

Usage: python compute_statistics.py fileWithData.txt

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


def compute_mean(numbers):
    """
    Compute the mean of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    return sum(numbers) / len(numbers) if numbers else None


def compute_median(numbers):
    """
    Compute the median of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The median of the numbers.
    """
    sorted_numbers = sorted(numbers)
    number = len(sorted_numbers)
    if number % 2 == 0:
        return (sorted_numbers[number // 2-1] + sorted_numbers[number//2])/2
    return sorted_numbers[number // 2]


def compute_mode(numbers):
    """
    Compute the mode of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: The mode(s) of the numbers.
    """
    if not numbers:
        return None
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    mode = [k for k, v in frequency.items() if v == max_frequency]
    if len(mode) == 1:
        return mode[0]  # If there's only one mode, return it directly
    return mode[0]


def compute_standard_deviation(numbers, mean):
    """
    Compute the standard deviation of a list of numbers.

    Args:
        numbers (list): A list of numbers.
        mean (float): The mean of the numbers.

    Returns:
        float: The standard deviation of the numbers.
    """
    variance = sum(
        (x-mean)**2 for x in numbers)/len(numbers) if numbers else None
    return variance ** 0.5 if variance else None


def compute_variance(numbers, mean):
    """
    Compute the variance of a list of numbers.

    Args:
        numbers (list): A list of numbers.
        mean (float): The mean of the numbers.

    Returns:
        float: The variance of the numbers.
    """
    return sum(
        (x-mean)**2 for x in numbers) / len(numbers) if numbers else None


def process_file(file_path):
    """
    Process a file to compute descriptive statistics.

    Args:
        file_path (str): The path to the file to process.
    """
    numbers = read_file(file_path)
    count = len(numbers)  # Calculate the count of numbers
    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    standard_deviation = compute_standard_deviation(numbers, mean)

    print("Descriptive Statistics:")
    print(f"Count: {count}")  # Display the count of numbers
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {standard_deviation}")

    with open("StatisticsResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write("Descriptive Statistics:\n")
        result_file.write(f"Count: {count}\n")  # Write the count to the file
        result_file.write(f"Mean: {mean}\n")
        result_file.write(f"Median: {median}\n")
        result_file.write(f"Mode: {mode}\n")
        result_file.write(f"Variance: {variance}\n")
        result_file.write(f"Standard Deviation: {standard_deviation}\n")


def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("Usage: python compute_statistics.py fileWithData.txt")
        return

    if not file_path:
        print("No file selected.")
        return

    start_time = time.time()

    process_file(file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Time elapsed: {elapsed_time} seconds")

    with open("StatisticsResults.txt", 'a', encoding='utf-8') as result_file:
        result_file.write(f"Time elapsed: {elapsed_time} seconds\n")


if __name__ == "__main__":
    main()
