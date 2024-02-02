"""
Counts the frequency of distinct words in a file.

This script reads words from a file, identifies all distinct words, and
calculates the frequency of each word. The results are printed on the
screen and saved in a file named WordCountResults.txt.

Usage: python word_count.py fileWithData.txt

Author: Najk
Date: 01-02-2024.
"""

import sys
import time


def read_file(file_name):
    """
    Read words from a file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A list of words read from the file.
    """
    words = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                for word in line.split():
                    words.append(word)
    except FileNotFoundError:
        print("File not found.")
    return words


def count_words(words):
    """
    Count the frequency of each word in a list.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary where keys are words
        and values are their frequencies.
    """
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def process_file(file_name):
    """
    Process a file to count the frequency of distinct words.

    Args:
        file_name (str): The name of the file to process.
    """
    words = read_file(file_name)
    word_count = count_words(words)

    with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write("Word Count Results:\n")
        result_file.write("Row Labels\tCount of "+file_name.strip('.txt')+"\n")
        for word, count in word_count.items():
            result_file.write(f"{word}\t\t{count}\n")

    print("Word Count Results:")
    print("Row Labels\tCount of FileName")
    for word, count in word_count.items():
        print(f"{word}\t\t{count}")


def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return

    file_name = sys.argv[1]

    start_time = time.time()

    process_file(file_name)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Time elapsed: {elapsed_time} seconds")

    with open("WordCountResults.txt", 'a', encoding='utf-8') as result_file:
        result_file.write(f"Time elapsed: {elapsed_time} seconds\n")

if __name__ == "__main__":
    main()
