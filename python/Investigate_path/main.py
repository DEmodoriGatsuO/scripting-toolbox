import os
import csv
from typing import List, Tuple
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def investigate_corrupted_path(file_path: str) -> List[str]:
    """
    Investigates the corrupted path by checking each folder until '?' is encountered.
    
    Args:
    file_path (str): The file path to investigate.
    
    Returns:
    List[str]: A list of valid directories until the path becomes corrupted (contains '?').
    """
    norm_path = os.path.normpath(file_path)
    path_parts = norm_path.split(os.sep)
    valid_path = ""
    valid_folders = []

    for part in path_parts:
        if '?' in part:
            break
        valid_path = os.path.join(valid_path, part)
        if os.path.exists(valid_path):
            valid_folders.append(valid_path)
        else:
            break

    return valid_folders

def investigate_paths_in_csv(input_csv: str, output_csv: str = None) -> List[Tuple[str, str]]:
    """
    Investigates all file paths in the input CSV and outputs the valid directories up to the corrupted part.
    
    Args:
    input_csv (str): Path to the input CSV file containing file paths.
    output_csv (str, optional): Path to save the output CSV file with results. If None, results will be printed.
    
    Returns:
    List[Tuple[str, str]]: A list of tuples containing the original path and the last valid folder.
    """
    results = []

    try:
        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            file_paths = [row[0] for row in reader]
    except Exception as e:
        logging.error(f"Error reading input file {input_csv}: {e}")
        return results

    for file_path in file_paths:
        print('?' in file_path)
        valid_folders = investigate_corrupted_path(file_path)
        last_valid_folder = valid_folders[-1] if valid_folders else "No valid folder found"
        results.append((file_path, last_valid_folder))

    if output_csv:
        try:
            with open(output_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Original Path', 'Last Valid Folder'])
                writer.writerows(results)
            logging.info(f"Results saved to {output_csv}")
        except Exception as e:
            logging.error(f"Error writing to output file {output_csv}: {e}")
    else:
        for original_path, last_valid_folder in results:
            logging.info(f"Original Path: {original_path}, Last Valid Folder: {last_valid_folder}")

    return results

if __name__ == "__main__":
    input_csv = 'file_paths.csv'
    output_csv = 'valid_folder_paths.csv'
    investigate_paths_in_csv(input_csv, output_csv)