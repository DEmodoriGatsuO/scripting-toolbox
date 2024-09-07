def check_password_protected(file_path):
    try:
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path) as zf:
                zf.testzip()
            return False, None  # Password not protected
        elif file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            return reader.is_encrypted, None
        elif file_path.endswith((".docx", ".xlsx")):
            with open(file_path, "rb") as f:
                office_file = msoffcrypto.OfficeFile(f)
                return office_file.is_encrypted(), None
        elif file_path.endswith((".xls", ".ppt")):
            ole = olefile.OleFileIO(file_path)
            if ole.exists('WordDocument'):
                return ole.get_type('WordDocument') == "StrongEncryptedPackage", None
            return False, None
        else:
            return False, "Unsupported file type"
    except Exception as e:
        return False, f"Error: {str(e)}"
        
        
def scan_directory(folder_path):
    results = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            is_protected, error_message = check_password_protected(file_path)
            if error_message:
                results.append([file_path, error_message])
            else:
                results.append([file_path, is_protected])
    return results

def save_results_to_csv(results, output_csv):
    try:
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["File Path", "Password Protected/Error"])
            writer.writerows(results)
        print(f"Results saved to {output_csv}")
    except IOError as e:
        print(f"Error saving results to CSV: {e}")
        
    import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder_path> <output_csv>")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_csv = sys.argv[2]
    
    results = scan_directory(folder_path)
    save_results_to_csv(results, output_csv)
        