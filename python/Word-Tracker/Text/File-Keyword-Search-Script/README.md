# File Keyword Search Script

This Python script processes a large number of text and CSV files, searching for specific keywords within them. It utilizes multiprocessing to speed up the process and supports different file encodings. The script reads file paths from a CSV file, checks for the presence of specific keywords, and writes the results to a CSV file.

## Features

- **Encoding Detection**: Automatically detects the encoding of files (supports UTF-8, Shift-JIS, EUC-JP, and ISO2022-JP, with fallback to `chardet` for other encodings).
- **Keyword Search**: Searches for specified keywords in the provided files.
- **Multiprocessing**: Processes files in parallel using multiple CPU cores for faster execution.
- **Progress Tracking**: Displays the processing progress using the `tqdm` library.
- **Logging**: Logs the processing status, errors, and results into a log file (`file_processing.log`).
- **CSV Output**: Outputs the search results into a CSV file.

## Requirements

- Python 3.x
- Required libraries:
  - `tqdm` (for progress tracking)
  - `chardet` (for encoding detection)
  
To install the required libraries, use:
```bash
pip install tqdm chardet
```

## Usage

1. **Prepare the Input File**: 
   - The script expects a CSV file (`file_paths.csv`) containing a list of file paths, one per line.
   - Example `file_paths.csv`:
     ```
     /path/to/file1.txt
     /path/to/file2.csv
     /path/to/file3.txt
     ```

2. **Define the Keywords**:
   - You need to define two lists of keywords to search for in the files (`word1_list` and `word2_list`).
   - Modify the script or pass the appropriate lists:
     ```python
     word1_list = ['keyword1', 'alias1']
     word2_list = ['keyword2', 'alias2']
     ```

3. **Run the Script**:
   - Execute the script by running:
     ```bash
     python script_name.py
     ```

4. **Output**:
   - The script will output the results to a CSV file (`results.csv`), containing:
     - Timestamp: When the file was processed.
     - File Path: Path to the processed file.
     - Status: Whether the file was successfully processed (`Success` or `Failure`).
     - Matched: The keywords found in the file (or 'None' if no matches were found).
     - Error Message: Any error encountered during processing.

## Example

### Input (file_paths.csv):
```
/path/to/file1.txt
/path/to/file2.csv
```

### Output (results.csv):
```
Timestamp,File Path,Status,Matched,Error Message
2024-09-19 14:00:00,/path/to/file1.txt,Success,keyword1,None
2024-09-19 14:00:05,/path/to/file2.csv,Failure,None,File does not exist
```

## Code Breakdown

- **`detect_encoding_fast(file_path)`**: 
  - Detects the encoding of the file using common encodings like UTF-8, Shift-JIS, etc. If the encoding cannot be determined, it uses `chardet` as a fallback.

- **`check_words_in_file(file_path, word1_list, word2_list)`**:
  - Checks if any of the keywords in `word1_list` or `word2_list` are present in the file. Returns a list of matched keywords or an error message if an issue occurred.

- **`process_single_file(file_path, word1_list, word2_list)`**:
  - Processes a single file to detect keywords and records the results.

- **`process_file_paths(input_file, word1_list, word2_list, output_file)`**:
  - Reads the input CSV, processes each file using multiprocessing, and writes the results to an output CSV.

## Logging

- The script logs all processing details and errors to `file_processing.log`. This file will record any issues encountered during file processing and general progress.

## Customization

- **Keyword Lists**: You can customize the `word1_list` and `word2_list` with the keywords you want to search for in the files.
- **Encoding Detection**: If your files use different encodings, you may modify the `common_encodings` list in the `detect_encoding_fast` function to include other encodings.

## Troubleshooting

- **Encoding Issues**: If the script fails to detect the encoding of certain files, you can manually add the required encoding to the `common_encodings` list or rely on `chardet`.
- **Missing Files**: The script will log and handle cases where a file doesn't exist or cannot be accessed.

## License

This project is licensed under the MIT License.
