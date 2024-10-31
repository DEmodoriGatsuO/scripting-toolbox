import os
import csv
import logging
import multiprocessing
from datetime import datetime
from typing import List
from functools import partial
from tqdm import tqdm

# Library for fast encoding detection
import codecs

# Configure logging
logging.basicConfig(filename='file_processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def detect_encoding_fast(file_path, bytes_to_read=1024):
    """
    Quickly detect the encoding of a file.

    - Attempts common encodings first.
    - Reads only part of the file for detection.

    Args:
    - file_path (str): The path to the file to detect the encoding of.
    - bytes_to_read (int): The number of bytes to read for detection.

    Returns:
    - str: The detected encoding, or None if detection fails.
    """
    common_encodings = ['utf-8', 'shift_jis', 'euc-jp', 'iso2022_jp']
    with open(file_path, 'rb') as f:
        raw = f.read(bytes_to_read)
    for enc in common_encodings:
        try:
            raw.decode(enc)
            return enc
        except UnicodeDecodeError:
            continue
    # If common encodings don't work, use chardet
    try:
        import chardet
        result = chardet.detect(raw)
        return result['encoding']
    except Exception as e:
        logging.error(f"Encoding detection failed for {file_path}: {e}")
        return None

def check_words_in_file(file_path, word1_list, word2_list):
    """
    Check if specific keywords exist in the file.

    Args:
    - file_path (str): The path to the file to check.
    - word1_list (list): First list of words to search for.
    - word2_list (list): Second list of words to search for.

    Returns:
    - tuple:
      - bool: True if any keywords were found.
      - list: List of found keywords.
      - str: Error message, if any (None if no error).
    """
    matched_words = []
    try:
        encoding = detect_encoding_fast(file_path)
        if not encoding:
            return False, [], f"Failed to detect encoding: {file_path}"

        with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
            for line in f:
                # Search for keywords
                for word in word1_list + word2_list:
                    if word in line:
                        matched_words.append(word)
                # Exit early if any keywords are found
                if matched_words:
                    break
        return len(matched_words) > 0, matched_words, None
    except Exception as e:
        logging.error(f"Error occurred while processing file {file_path}: {e}")
        return False, [], str(e)

def process_single_file(file_path, word1_list, word2_list):
    """
    Process a single file.

    Args:
    - file_path (str): The path to the file to process.
    - word1_list (list): First list of keywords to search for.
    - word2_list (list): Second list of keywords to search for.

    Returns:
    - list: The result of the processing.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if os.path.exists(file_path):
        logging.info(f"Processing file {file_path}")
        status, matched_words, error_message = check_words_in_file(file_path, word1_list, word2_list)
        status_text = "Success" if status else "Failure"
        matched_str = ','.join(matched_words) if matched_words else 'None'
        result = [timestamp, file_path, status_text, matched_str, error_message or '']
        logging.info(f"Result for file {file_path}: {status_text}, Matches: {matched_str}")
    else:
        error_message = f"File does not exist: {file_path}"
        logging.error(error_message)
        result = [timestamp, file_path, "Failure", 'None', error_message]
    return result

def process_file_paths(input_file: str, word1_list: List[str], word2_list: List[str], output_file=None):
    """
    Read file paths, process each file, and output the results.

    Args:
    - input_file (str): Input file containing file paths (CSV).
    - word1_list (list): First list of keywords to search for.
    - word2_list (list): Second list of keywords to search for.
    - output_file (str, optional): Path to the output CSV file.

    Returns:
    - None
    """
    # Read file paths
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            file_paths = [row[0] for row in reader]
    except Exception as e:
        logging.error(f"Error reading input file {input_file}: {e}")
        return

    # Create a multiprocessing pool
    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(cpu_count)

    # Create a partially applied function
    func = partial(process_single_file, word1_list=word1_list, word2_list=word2_list)

    # Display progress with tqdm
    results = []
    for result in tqdm(pool.imap_unordered(func, file_paths), total=len(file_paths)):
        results.append(result)

    pool.close()
    pool.join()

    # Output results
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
        for result in results:
            print(result)

if __name__ == "__main__":
    input_file = 'file_paths.csv'
    # List of keywords to search for
    word1_list = ['keyword1', 'alias1']
    word2_list = ['keyword2', 'alias2']
    # Path to the output file
    output_file = 'results.csv'

    process_file_paths(input_file, word1_list, word2_list, output_file)
