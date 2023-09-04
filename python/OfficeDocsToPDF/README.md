# OfficeDocsToPDF

OfficeDocsToPDF is a Python script that converts PowerPoint, Word, and Excel files to PDF format. It provides a convenient way to convert various Office documents into a more widely supported PDF format.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This script allows you to convert PowerPoint (.ppt, .pptx), Word (.doc, .docx), and Excel (.xls, .xlsx) files to PDF format. The script utilizes the `comtypes` library to interact with Microsoft Office applications and automate the conversion process.

## Requirements

- Python 3.x
- `comtypes` library (Install using `pip install comtypes`)

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Install the required `comtypes` library by running: `pip install comtypes`
3. Place your PowerPoint, Word, and Excel files in a single folder.
4. Open a terminal/command prompt and navigate to the folder containing the script.
5. Run the script using the following command:

   ```sh
   python OfficeDocsToPDF.py <input_folder_path>
   ```

   Replace `OfficeDocsToPDF.py` with the actual name of the script file and `<input_folder_path>` with the path to the folder containing the Office documents you want to convert.

6. The script will create a timestamped output folder containing the converted PDF files.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/OfficeDocsToPDF.git
   ```

2. Navigate to the project directory:

   ```sh
   cd OfficeDocsToPDF
   ```

3. Install the required `comtypes` library:

   ```sh
   pip install comtypes
   ```

## License

Free