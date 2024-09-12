import requests
import socket
import logging
from datetime import datetime

def send_results_to_api(api_url: str, start_time: datetime, end_time: datetime, total_files: int, error_count: int, input_file: str) -> None:
    data = {
        "start_time": start_time.strftime('%Y-%m-%d %H:%M:%S'),
        "end_time": end_time.strftime('%Y-%m-%d %H:%M:%S'),
        "total_files": total_files,
        "error_count": error_count,
        "input_file": input_file,
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