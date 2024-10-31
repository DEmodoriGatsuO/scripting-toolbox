import os
import logging
from typing import List, Tuple, Optional
from pyxlsb import open_workbook

def check_words_in_xlsb(file_path: str, word1_list: List[str], word2_list: List[str]) -> Tuple[bool, List[str], Optional[str]]:
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
    from datetime import datetime
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