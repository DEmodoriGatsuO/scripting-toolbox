import os
import csv
import chardet
import logging
from datetime import datetime
from typing import List

# Configure logging
logging.basicConfig(filename='file_processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def detect_encoding(file_path):
    """
    Detect the encoding of a file automatically.
    
    Args:
    - file_path (str): The path to the file whose encoding needs to be detected.

    Returns:
    - str: The detected encoding of the file, or None if detection fails.
    """
    try:
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            return result['encoding']
    except Exception as e:
        logging.error(f"Error detecting encoding for the file: {e}")
        return None

def check_words_in_file(file_path, word1_list, word2_list):
    """
    Check if any words from word1_list or word2_list are present in the given file.
    
    Args:
    - file_path (str): The path to the file to be checked.
    - word1_list (list): The first list of words to search for.
    - word2_list (list): The second list of words to search for.

    Returns:
    - tuple:
      - bool: True if any word from either list is found, False otherwise.
      - list: A list of words that were found in the file.
      - str: An error message if an exception occurs, otherwise None.
    """
    matched_words = []  # List to store matched words
    try:
        # Detect the encoding of the file
        encoding = detect_encoding(file_path)
        if not encoding:
            return False, [], f"Could not detect encoding: {file_path}"

        # Open the file with the detected encoding and check for words
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
            
            # Check for matches in word1_list
            for word1 in word1_list:
                if word1 in content:
                    matched_words.append(word1)

            # Check for matches in word2_list
            for word2 in word2_list:
                if word2 in content:
                    matched_words.append(word2)

            return len(matched_words) > 0, matched_words, None
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        return False, [], str(e)

def process_file_paths(input_file: str, word1_list: List[str], word2_list: List[str], output_file=None):
    """
    Read file paths from the input file, check for specified words in each file,
    and output the results to a CSV file or print them to the console.
    
    Args:
    - input_file (str): Path to the input file containing file paths (CSV or text).
    - word1_list (list): List of words to search for.
    - word2_list (list): Another list of words to search for.
    - output_file (str, optional): Path to the output CSV file. If None, results will be printed.

    Returns:
    - None
    """
    results = []

    # Read input file and determine if it's a CSV or text file
    try:
        with open(input_file, 'rb') as f:
            # Detect encoding of the input file
            raw_data = f.read()
            detected = chardet.detect(raw_data)
            encoding = detected['encoding']
        
        # Open the input file with the detected encoding
        with open(input_file, 'r', encoding=encoding) as f:
            if input_file.endswith('.csv'):
                reader = csv.reader(f)
                file_paths = [row[0] for row in reader]
            else:
                file_paths = [line.strip() for line in f.readlines()]
    except Exception as e:
        logging.error(f"Error reading input file {input_file}: {e}")
        return

    # Process each file path and check for words
    for file_path in file_paths:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if os.path.exists(file_path):
            logging.info(f"Processing file {file_path}")
            status, matched_words, error_message = check_words_in_file(file_path, word1_list, word2_list)
            status_text = "Success" if status else "Failure"
            matched_str = ','.join(matched_words) if matched_words else 'None'
            results.append([timestamp, file_path, status_text, matched_str, error_message or ''])
            logging.info(f"Result for file {file_path}: {status_text}, Matches: {matched_str}")
        else:
            error_message = f"File does not exist: {file_path}"
            logging.error(error_message)
            results.append([timestamp, file_path, "Failure", 'None', error_message])

    # Output results to CSV or print to console
    if output_file:
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'File Path', 'Status', 'Matched', 'Error Message'])
                writer.writerows(results)
            logging.info(f"Results written to {output_file}")
        except Exception as e:
            logging.error(f"Error writing to output file {output_file}: {e}")
    else:
        # Print results to console
        print("File paths and search results:")
        for result in results:
            print(result)

if __name__ == "__main__":
    input_file = 'file_paths.csv'
    # List of words to search for
    word1_list = ['word1', 'alias1']
    # Another list of words to search for
    word2_list = ['word2', 'alias2']
    # Set to None if you don't want CSV output
    output_file = 'results.csv'

    process_file_paths(input_file, word1_list, word2_list, output_file)