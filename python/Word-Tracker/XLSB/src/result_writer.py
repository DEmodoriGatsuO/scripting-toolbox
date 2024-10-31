import csv
from typing import List, Tuple
import logging

def write_results_to_csv(output_file: str, results: List[Tuple[str, str, str, str, str]]) -> None:
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'File Path', 'Status', 'Matched', 'Error Message'])
            writer.writerows(results)
        logging.info(f"Results written to {output_file}")
    except Exception as e:
        logging.error(f"Error occurred while writing output file {output_file}: {e}")