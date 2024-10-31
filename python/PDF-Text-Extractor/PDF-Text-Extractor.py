"""
 Project Name    : PDF-Text-Extractor
 File Name       : PDF-Text-Extractor.py
 Feature         : Extract text from a PDF file and save it to a text file.
 Creation Date   : 2023.08.29
 Programming language used:
  
 Author          : DEmodoriGatsuO https://github.com/DEmodoriGatsuO
 Twitter         : https://twitter.com/DemodoriGatsuo Follow Me!
 Sorry           : I like English. But I can't use English.
 
 Copyright (c) 2023, Tech Lovers. All rights reserved
 I can't use English, so I'll write in Japanese from now on.
"""

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
        'initialdir':  os.getcwd() 
    }

    # Open file dialog to choose a PDF file
    pdf_path = filedialog.askopenfilename(**file_options)
    
    if pdf_path:
        # Define the output text file path
        output_path = os.path.join(os.getcwd(), 'pdf_extracted_text.txt')

        # Extract text from the PDF and save it to the output file
        extract_pdf_text(pdf_path, output_path)

        # Show completion message
        messagebox.showinfo('Complete', 'PDF text extraction completed.\nOutput saved to pdf_extracted_text.txt')

if __name__ == "__main__":
    main()
