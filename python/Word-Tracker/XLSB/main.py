import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Optional
import os

from src.file_processor import process_single_file
from src.file_reader import read_file_paths
from src.result_writer import write_results_to_csv
from src.api_client import send_results_to_api

logging.basicConfig(filename='xlsb_processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_xlsb_files(input_file: str, word1_list: List[str], word2_list: List[str], output_file: Optional[str] = None, api_url: Optional[str] = None, max_workers: int = 5) -> None:
    start_time = datetime.now()
    total_files = 0
    error_count = 0

    file_paths = read_file_paths(input_file)
    if not file_paths:
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
        write_results_to_csv(output_file, results)
    else:
        print("File paths and search results:")
        for result in results:
            print(result)

    end_time = datetime.now()

    if api_url:
        send_results_to_api(api_url, start_time, end_time, total_files, error_count, os.path.basename(input_file))

if __name__ == "__main__":
    input_file = 'xlsb_file_paths.csv'
    word1_list = ['word1', 'alias1']
    word2_list = ['word2', 'alias2']
    output_file = 'xlsb_results.csv'
    api_url = 'https://api.example.com/results'
    max_workers = 5

    process_xlsb_files(input_file, word1_list, word2_list, output_file, api_url, max_workers)