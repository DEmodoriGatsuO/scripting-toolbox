# XLSB Word Checker

## Overview

XLSB Word Checker is a Python-based tool designed to search for specific words within XLSB (Excel Binary) files. It provides efficient processing of multiple files, supports parallel execution, and offers optional API integration for result reporting.

## Features

- Search for specified words in XLSB files
- Process multiple files in parallel for improved performance
- Support for both CSV and text file inputs containing file paths
- Optional CSV output for search results
- API integration for sending processing statistics
- Comprehensive logging for monitoring and debugging

## Requirements

- Python 3.7+
- pyxlsb
- requests

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/xlsb-word-checker.git
   cd xlsb-word-checker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your input file (CSV or text) containing the paths of XLSB files to be processed.

2. Run the script:
   ```
   python main.py
   ```

3. The script will prompt you for the following information:
   - Path to the input file
   - Words to search for (separated by commas)
   - Output file path (optional)
   - API URL for sending results (optional)
   - Number of worker threads for parallel processing

## Configuration

You can modify the following parameters in the `config.yaml` file:

- `max_workers`: Maximum number of parallel threads (default: 5)
- `log_file`: Path to the log file
- `default_input_file`: Default path for the input file
- `default_output_file`: Default path for the output file

## Output

The tool generates two types of output:

1. CSV file (if specified) containing:
   - Timestamp
   - File Path
   - Status (Success/Failure)
   - Matched Words
   - Error Message (if any)

2. API POST request (if URL provided) with:
   - Start Time
   - End Time
   - Total Files Processed
   - Error Count
   - Input File Name
   - Host Name

## Logging

The script logs its operations to `xlsb_processing.log`. Check this file for detailed information about the processing steps and any errors encountered.

## Contributing

Contributions to improve XLSB Word Checker are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` file for more information.