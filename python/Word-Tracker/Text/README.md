# Text word tracker

## Overview
This Python script reads a list of file paths, checks for specific words in each file, and outputs the results to a CSV file or prints them to the console. It includes automatic encoding detection and logs the processing progress and any errors encountered.

## Features
- Detects file encoding using `chardet`.
- Searches for specific words in text or CSV files.
- Outputs results to a CSV file or console.
- Logs all operations and errors.
  
## Dependencies
- Python 3.x
- External libraries:
  - `chardet` (for detecting file encoding)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Install the required dependencies:
   ```bash
   pip install chardet
   ```

## Usage
1. **Prepare input file**:  
   - Create a CSV or text file that contains a list of file paths (one file path per row).

2. **Edit script**:  
   Modify the variables in the script:
   - `input_file`: Path to the input CSV or text file containing file paths.
   - `word1_list`: List of words to search for.
   - `word2_list`: Another list of words to search for.
   - `output_file`: Optional. Path to the output CSV file. If set to `None`, results will be printed to the console.

3. **Run the script**:
   ```bash
   python script.py
   ```

### Example
```python
input_file = 'file_paths.csv'
word1_list = ['word1', 'alias1']
word2_list = ['word2', 'alias2']
output_file = 'results.csv'

process_file_paths(input_file, word1_list, word2_list, output_file)
```

## Functions

### `detect_encoding(file_path)`
- Detects the encoding of the specified file.
- **Input**: `file_path` (str)
- **Output**: Detected encoding (str), or `None` if detection fails.

### `check_words_in_file(file_path, word1_list, word2_list)`
- Checks if any words from `word1_list` or `word2_list` exist in the file.
- **Input**: `file_path` (str), `word1_list` (list), `word2_list` (list)
- **Output**: Tuple (`status` (bool), `matched_words` (list), `error_message` (str))

### `process_file_paths(input_file, word1_list, word2_list, output_file=None)`
- Processes file paths from the input file, checks for words, and outputs results to CSV or console.
- **Input**: `input_file` (str), `word1_list` (list), `word2_list` (list), `output_file` (str or `None`)
- **Output**: Results logged to a CSV file or printed to the console.

## Logging
- Logs are stored in `file_processing.log`.
- Logs include processing results, errors, and timestamps.

## Error Handling
- The script handles file reading and encoding detection errors gracefully and logs them.

## Future Improvements
- Add retry mechanism for failed file operations.
- Optimize for large-scale file processing.
- Add support for regular expressions in word search.

## License
This project is licensed under the MIT License.
```

This README is concise and provides clear instructions on how to use the script, including installation, usage, and a brief description of its functions.