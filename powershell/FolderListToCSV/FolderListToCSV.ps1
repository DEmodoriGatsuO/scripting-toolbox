<#
Script: FolderListToCSV.ps1
Author: ChatGPT
Tester: Demodori Gatsuo

Description:
This script recursively retrieves the list of subfolders and files in a specific folder and outputs the information as a CSV file.

Output format:
- FullPath: The full path of the file or folder.
- SubfolderName: The name of the subfolder that contains the file.
- FileName: The name of the file.
- Extension: The extension of the file.

Instructions:
1. Set the folderPath variable to the path of the folder you want to retrieve the list from.
2. Set the csvPath variable to the path where you want to save the CSV file.
3. Run the script.

Note: Make sure to have the appropriate permissions to access the folders and files.

#>

# Set the folder path to retrieve the list from
$folderPath = "C:\Path\To\Your\Folder"

# Set the CSV file path for output
$csvPath = "C:\Path\To\Output\File.csv"

# Retrieve the list of folders and files recursively and create CSV data
$data = Get-ChildItem -Path $folderPath -Recurse | ForEach-Object {
    $item = $_
    $folderName = Split-Path -Path $item.FullName -Leaf

    # For files
    if ($item.PSIsContainer -eq $false) {
        $subfolderName = Split-Path -Path $item.Directory.FullName -Leaf
        $extension = [System.IO.Path]::GetExtension($item.Name)
        $row = [PSCustomObject]@{
            "FullPath" = $item.FullName
            "SubfolderName" = $subfolderName
            "FileName" = $item.Name
            "Extension" = $extension
        }
        $row
    }
    # For folders
    else {
        $row = [PSCustomObject]@{
            "FullPath" = $item.FullName
            "SubfolderName" = $folderName
            "FileName" = ""
            "Extension" = ""
        }
        $row
    }
}

# Write the data to the CSV file
$data | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8
