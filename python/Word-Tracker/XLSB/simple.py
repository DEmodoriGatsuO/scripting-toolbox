import os
import csv
import logging
import socket
import requests
from datetime import datetime
from pyxlsb import open_workbook
from typing import List, Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configure logging
logging.basicConfig(filename='xlsb_processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_words_in_xlsb(file_path: str, word1_list: List[str], word2_list: List[str]) -> Tuple[bool, List[str], Optional[str]]:
    """
    Check if any words from word1_list or word2_list are present in any sheet of the specified XLSB file.
    
    Args:
        file_path (str): Path to the XLSB file to be checked.
        word1_list (List[str]): The first list of words to search for.
        word2_list (List[str]): The second list of words to search for.

    Returns:
        Tuple[bool, List[str], Optional[str]]:
            - bool: True if any word from the lists is found, False otherwise.
            - List[str]: List of matched words.
            - Optional[str]: Error message if an exception occurs, otherwise None.
    """
    matched_words = set()
    try:
        with open_workbook(file_path) as wb:
            for sheet in wb.sheets:
                with wb.get_sheet(sheet) as sheet:
                    for row in sheet.rows():
                        for cell in row:
                            if cell and isinstance(cell.v, str):
                                cell_value = cell.v.lower()
                                matched_words.update(word for word in word1_list + word2_list 
                                                     if word.lower() in cell_value)

        return bool(matched_words), list(matched_words), None
    except Exception as e:
        error_message = f"Error occurred while processing file {file_path}: {str(e)}"
        logging.error(error_message)
        return False, [], error_message

def process_single_file(file_path: str, word1_list: List[str], word2_list: List[str]) -> Tuple[str, str, str, str, str]:
    """
    Process a single XLSB file and return the result.

    Args:
        file_path (str): Path to the XLSB file.
        word1_list (List[str]): The first list of words to search for.
        word2_list (List[str]): The second list of words to search for.

    Returns:
        Tuple[str, str, str, str, str]: Timestamp, file path, status, matched words, error message.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if os.path.exists(file_path) and file_path.lower().endswith('.xlsb'):
        logging.info(f"Processing file {file_path}")
        status, matched_words, error_message = check_words_in_xlsb(file_path, word1_list, word2_list)
        status_text = "Success" if status else "Failure"
        matched_str = ','.join(matched_words) if matched_words else 'None'
        logging.info(f"Result for file {file_path}: {status_text}, Matches: {matched_str}")
    else:
        error_message = f"File does not exist or is not an XLSB file: {file_path}"
        logging.error(error_message)
        status_text = "Failure"
        matched_str = 'None'
    
    return timestamp, file_path, status_text, matched_str, error_message or ''

def process_xlsb_files(input_file: str, word1_list: List[str], word2_list: List[str], output_file: Optional[str] = None, api_url: Optional[str] = None, max_workers: int = 5) -> None:
    """
    Read file paths from the input file, check each XLSB file for specified words, and log the results.
    Optionally, save the results to a CSV and send summary statistics to an API.
    
    Args:
        input_file (str): Path to the input file containing the list of XLSB file paths (CSV or text).
        word1_list (List[str]): The first list of words to search for.
        word2_list (List[str]): The second list of words to search for.
        output_file (Optional[str]): Path to save the results to a CSV file. If None, results are printed to the console.
        api_url (Optional[str]): URL to send the summary statistics to an API. If None, no API call is made.
        max_workers (int): Maximum number of worker threads for parallel processing.

    Returns:
        None
    """
    start_time = datetime.now()
    total_files = 0
    error_count = 0

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            file_paths = csv.reader(f) if input_file.endswith('.csv') else f
            file_paths = [row[0] if isinstance(row, list) else row.strip() for row in file_paths]
    except Exception as e:
        logging.error(f"Error occurred while reading input file {input_file}: {e}")
        return

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {executor.submit(process_single_file, file_path, word1_list, word2_list): file_path for file_path in file_paths}
        for future in as_completed(future_to_file):
            total_files += 1
            result = future.result()
            results.append(result)
            if result[2] == "Failure":
                error_count += 1

    if output_file:
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'File Path', 'Status', 'Matched', 'Error Message'])
                writer.writerows(results)
            logging.info(f"Results written to {output_file}")
        except Exception as e:
            logging.error(f"Error occurred while writing output file {output_file}: {e}")
    else:
        print("File paths and search results:")
        for result in results:
            print(result)

    end_time = datetime.now()

    if api_url:
        data = {
            "start_time": start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": end_time.strftime('%Y-%m-%d %H:%M:%S'),
            "total_files": total_files,
            "error_count": error_count,
            "input_file": os.path.basename(input_file),
            "host_name": socket.gethostname()
        }
        try:
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                logging.info(f"Successfully posted results to API: {api_url}")
            else:
                logging.error(f"Failed to post results to API. Status code: {response.status_code}")
        except Exception as e:
            logging.error(f"Error occurred while posting results to API: {str(e)}")

if __name__ == "__main__":
    input_file = 'xlsb_file_paths.csv'
    word1_list = ['word1', 'alias1']
    word2_list = ['word2', 'alias2']
    output_file = 'xlsb_results.csv'
    api_url = 'https://api.example.com/results'
    max_workers = 5

    process_xlsb_files(input_file, word1_list, word2_list, output_file, api_url, max_workers)