# Define the source folder containing HTML files and the wkhtmltopdf executable path
$sourceFolder = "C:\Path\To\FolderA"
$wkhtmltopdfPath = "C:\Path\To\wkhtmltopdf.exe"

# Create a new folder with the current date and time
$timestamp = Get-Date -Format "yyyyMMddHHmmss"
$destinationFolder = "C:\Path\To\NewFolder_$timestamp"
New-Item -Path $destinationFolder -ItemType Directory

# Iterate over each HTML file in the source folder
Get-ChildItem -Path $sourceFolder -Filter *.html | ForEach-Object {
    $htmlFilePath = $_.FullName
    $pdfFilePath = "$destinationFolder\$($_.BaseName).pdf"

    # Convert HTML to PDF
    & $wkhtmltopdfPath $htmlFilePath $pdfFilePath

    # Move the HTML file to the new folder
    Move-Item -Path $htmlFilePath -Destination $destinationFolder
}

# Output completion message
Write-Host "HTML files converted to PDF and moved to $destinationFolder"