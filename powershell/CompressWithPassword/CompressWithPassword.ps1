# Requires 7-Zip to be installed

param (
    [string]$filePath,  # Path to the file to be compressed
    [string]$password   # Password for the zip archive
)

# Check if 7-Zip is installed
$7zipPath = "C:\Program Files\7-Zip\7z.exe"
if (-not (Test-Path -Path $7zipPath)) {
    Write-Error "7-Zip is not installed."
    exit 1
}

# Create the zip file name from the original file name
$zipFileName = [System.IO.Path]::ChangeExtension($filePath, ".zip")

# Compress the file with password
& $7zipPath a -p$password -tzip $zipFileName $filePath

Write-Host "File compressed successfully: $zipFileName"
