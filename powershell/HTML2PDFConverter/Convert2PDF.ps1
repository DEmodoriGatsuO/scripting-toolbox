# Directory to monitor
$watchFolder = "C:\path\to\watch\folder"

# Create a Word application object
$word = New-Object -ComObject Word.Application
$word.Visible = $false

# Process all HTML files in the specified directory
Get-ChildItem -Path $watchFolder -Filter *.html | ForEach-Object {
    $htmlFilePath = $_.FullName
    $pdfFilePath = [System.IO.Path]::ChangeExtension($htmlFilePath, "pdf")

    # Skip if the PDF already exists
    if (Test-Path $pdfFilePath) {
        Continue
    }

    try {
        # Open the HTML file
        $document = $word.Documents.Open($htmlFilePath)

        # Save as PDF
        $document.SaveAs([ref] $pdfFilePath, [ref] 17) # 17 represents the PDF format

        # Close the document
        $document.Close()
    }
    catch {
        Write-Host "Error: $_"
    }
}

# Close the Word application
$word.Quit()

# Release the COM object
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()
