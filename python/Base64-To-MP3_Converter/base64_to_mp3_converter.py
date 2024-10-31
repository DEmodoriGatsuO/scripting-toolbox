# -----------------------------------------------------------------------------
# Script Name: base64_to_mp3_converter.py
# Description: A script to convert a base64-encoded string into an MP3 audio file
# Author: ChatGPT with De'modori Gatsuo
# Created Date: 2023.07.27
# -----------------------------------------------------------------------------

import base64

def convert_base64_to_mp3(base64_string, output_file):
    """
    Convert a base64-encoded string into an MP3 audio file.

    Parameters:
        base64_string (bytes): The base64-encoded string to decode, provided as bytes.
        output_file (str): The output filename to save the MP3 audio file.

    Returns:
        None
    """
    decoded_data = base64.b64decode(base64_string)  # Decode the base64-encoded string to binary data

    with open(output_file, "wb") as file:
        file.write(decoded_data)  # Write the binary data to an MP3 audio file

def main():
    base64_file = "input.txt"  # Input filename containing the base64-encoded string

    with open(base64_file, 'rb') as f:
        base64_string = f.read()  # Read the base64-encoded string from the input file

    output_file = "output.mp3"  # Output filename for the decoded MP3 audio file

    convert_base64_to_mp3(base64_string, output_file)  # Convert base64 to MP3 and save as a file

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly