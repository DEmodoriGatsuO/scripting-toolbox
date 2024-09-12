import csv
import logging
from typing import List

def read_file_paths(input_file: str) -> List[str]:
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            file_paths = csv.reader(f) if input_file.endswith('.csv') else f
            return [row[0] if isinstance(row, list) else row.strip() for row in file_paths]
    except Exception as e:
        logging.error(f"Error occurred while reading input file {input_file}: {e}")
        return []