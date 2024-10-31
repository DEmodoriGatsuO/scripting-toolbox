"""
Script Name: OfficeDocsToPDF.py
Author: Editor De'modori Gatsuo
Description: This script converts PowerPoint, Word, and Excel files in a specified folder to PDF format.

Requirements:
- Python 3.10
- comtypes library (Install using 'pip install comtypes')

Usage: python script_name.py <input_folder_path>

The script takes an input folder path as a command-line argument and creates a timestamped output folder
containing the converted PDF files.

"""

import sys
import os
import comtypes.client
import datetime

def main():
    dt_now = datetime.datetime.now()
    str_dt_now = dt_now.strftime('%Y%m%d%H%M%S')

    # Get input folder path from command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <input_folder_path>")
        sys.exit(1)
    input_folder_path = sys.argv[1]

    # Create output folder using timestamp
    file_folder_path = os.path.abspath(__file__)
    output_folder_path = os.path.join(os.path.dirname(file_folder_path), str_dt_now)
    os.mkdir(output_folder_path)

    office_applications = {
        "ppt": {"app_name": "Powerpoint.Application", "save_format": 32},
        "doc": {"app_name": "Word.Application", "save_format": 17},
        "xlsx": {"app_name": "Excel.Application", "save_format": 0}
    }

    for input_file_name in os.listdir(input_folder_path):
        input_file_path = os.path.join(input_folder_path, input_file_name)
        file_name, file_extension = os.path.splitext(input_file_name)
        output_file_path = os.path.join(output_folder_path, file_name + ".pdf")

        for app_key, app_data in office_applications.items():
            if input_file_name.lower().endswith(tuple("." + ext for ext in app_data["extensions"])):
                office_app = comtypes.client.CreateObject(app_data["app_name"])
                office_app.Visible = False if app_key != "ppt" else 1
                doc = office_app.Documents.Open(input_file_path) if app_key == "doc" else None
                wb = office_app.Workbooks.Open(input_file_path) if app_key == "xlsx" else None

                if app_key == "ppt":
                    presentation = office_app.Presentations.Open(input_file_path)
                    presentation.SaveAs(output_file_path, app_data["save_format"])
                    presentation.Close()
                elif app_key == "doc":
                    doc.SaveAs(output_file_path, app_data["save_format"])
                    doc.Close()
                elif app_key == "xlsx":
                    wb.ExportAsFixedFormat(0, output_file_path, 1, 0)
                    wb.Close()

                office_app.Quit()
                break

    print("Conversion Complete")

if __name__ == "__main__":
    main()
