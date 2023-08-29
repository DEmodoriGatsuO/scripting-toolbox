# GPT Prompts
 - This's my useful prompt for update scripts and documents.
 - Create by japanese



## example
```plane-text
あなたは熟練の[]のプログラマーです。下記のコードをあなたの熟練の知識と経験に基づき、コメントの付与、変数名や関数の名前をベストプラクティスに基づき、修正してください。
また先頭にスクリプトの名前や目的を記載してください。

You are a skilled [Sample] programmer. Please modify the code below based on your proficiency and experience, adding comments and naming variables and functions according to best practices.
Please also include the name and purpose of the script at the beginning.
-------------


```

# Script Name: PDF Text Extractor
# Purpose: This script extracts text from a selected PDF file using pdfminer and saves it to a text file.
# Author: [Your Name]
# Date: [Current Date]

import os
from pdfminer.high_level import extract_text
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_pdf_text(pdf_path, output_path):
    """
    Extract text from a PDF file and save it to a text file.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_path (str): Path to the output text file.
    """
    pdf_text = extract_text(pdf_path)

    with open(output_path, 'w', encoding='UTF-8', newline='\n') as f:
        f.write(pdf_text)

def main():
    # Initialize the tkinter GUI
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Define file dialog options
    file_options = {
        'filetypes': [('PDF Files', '*.pdf')],
        'initialdir': os.path.expanduser('~')  # Open user's home directory by default
    }

    # Open file dialog to choose a PDF file
    pdf_path = filedialog.askopenfilename(**file_options)
    
    if pdf_path:
        # Define the output text file path
        output_path = os.path.join(os.path.expanduser('~'), 'pdf_extracted_text.txt')

        # Extract text from the PDF and save it to the output file
        extract_pdf_text(pdf_path, output_path)

        # Show completion message
        messagebox.showinfo('Complete', 'PDF text extraction completed.\nOutput saved to pdf_extracted_text.txt')

if __name__ == "__main__":
    main()
