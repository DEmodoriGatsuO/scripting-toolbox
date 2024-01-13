# TextArchiveBuilder

TextArchiveBuilder is a versatile tool for merging multiple text files from a specified folder into a single consolidated text file while preserving the original file names for easy reference. This project simplifies the process of combining text documents and is useful for tasks such as aggregating logs, research notes, or any textual data stored in separate files.

## Features

- Merge multiple text files into a single output file.
- Include original file names as headers within the merged document.
- Add customizable separators between each file's content.
- Easy-to-use PowerShell script for efficient text file consolidation.

## Prerequisites

Before using TextArchiveBuilder, ensure you have the following requirements met:

- Windows operating system with PowerShell support.
- A folder containing the text files you want to merge.

## Getting Started

1. Clone or download this repository to your local machine.

2. Open a PowerShell terminal.

3. Navigate to the project directory:
   ```
   cd path\to\TextArchiveBuilder
   ```

4. Run the script with the following command, replacing placeholders with your specific folder and output file paths:
   ```
   .\Merge-TextFiles.ps1 -FolderPath "C:\your\folder\path" -OutputFilePath "C:\your\output\file.txt"
   ```

5. The merged text file will be created in the specified output location.

## Usage

To merge your text files using TextArchiveBuilder, follow these steps:

1. Modify the script if needed (e.g., customize separators or formatting).

2. Run the script with the appropriate folder path and output file path.

3. Review the merged file to see the consolidated content along with original file names for reference.

## Customization

You can customize TextArchiveBuilder by modifying the script. Open `Merge-TextFiles.ps1` and adjust the variables or formatting according to your preferences.

Happy text file merging with TextArchiveBuilder!
