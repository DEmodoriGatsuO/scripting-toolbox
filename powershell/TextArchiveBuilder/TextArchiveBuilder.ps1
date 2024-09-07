# Specify the folder path
$folderPath = "C:\folder\path"

# Specify the output path and filename for the merged file
$outputFilePath = "C:\output\file\path\merged_file.txt"

# Retrieve all text files in the folder and merge them
Get-ChildItem -Path $folderPath -Filter "*.txt" | ForEach-Object {
    # Insert the file name
    $fileName = $_.Name
    Add-Content -Path $outputFilePath -Value ("File Name: $fileName")
    
    # Insert the file content
    Get-Content $_.FullName | Add-Content -Path $outputFilePath
    Add-Content -Path $outputFilePath -Value "------------------------------------------"  # Separator between files
}

Write-Host "Text files have been merged. Output file: $outputFilePath"
