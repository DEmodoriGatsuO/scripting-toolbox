param (
    [string]$htmlFilePath
)

# Test Html Path
if (-not $htmlFilePath) {
    Write-Host "Error Html Path"
    exit
}

# Create PDF Path
$pdfFilePath = [System.IO.Path]::ChangeExtension($htmlFilePath, "pdf")

# Create a Word application object
$word = New-Object -ComObject Word.Application

try {
    # Word Visible
    $word.Visible = $false

    # Open HTML File
    $document = $word.Documents.Open($htmlFilePath)

    # Save as PDF file
    $document.SaveAs([ref] $pdfFilePath, [ref] 17) # 17 is PDF

    # Close html file
    $document.Close()
}
catch {
    Write-Host "Error: $_"
}
finally {
    # Finish Word Application
    $word.Quit()
}

# Check Result
if (Test-Path $pdfFilePath) {
    Write-Host "PDF Create Success: $pdfFilePath"
} else {
    Write-Host "PDF Create Failed"
}
