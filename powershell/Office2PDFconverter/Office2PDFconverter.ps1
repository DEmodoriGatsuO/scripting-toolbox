# PowerShell Script to Convert Excel, Word, and PowerPoint Files to PDF

# Specify the directory to search for files
$directory = "C:\Path\To\Your\Files"

# Create an instance of Word, Excel, and PowerPoint applications
$word = New-Object -ComObject Word.Application
$excel = New-Object -ComObject Excel.Application
$powerPoint = New-Object -ComObject PowerPoint.Application

# Hide the applications during processing
$word.Visible = $false
$excel.Visible = $false
$powerPoint.Visible = $false

# Function to convert Word documents to PDF
function Convert-WordToPDF($file) {
    $doc = $word.Documents.Open($file.FullName)
    $pdfPath = $file.DirectoryName + "\" + $file.BaseName + ".pdf"
    $doc.SaveAs([ref] $pdfPath, [ref] 17) # 17 is the enum for PDF format
    $doc.Close()
}

# Function to convert Excel workbooks to PDF
function Convert-ExcelToPDF($file) {
    $workbook = $excel.Workbooks.Open($file.FullName)
    $pdfPath = $file.DirectoryName + "\" + $file.BaseName + ".pdf"
    $workbook.ExportAsFixedFormat(0, $pdfPath) # 0 is the enum for PDF format
    $workbook.Close()
}

# Function to convert PowerPoint presentations to PDF
function Convert-PowerPointToPDF($file) {
    $presentation = $powerPoint.Presentations.Open($file.FullName)
    $pdfPath = $file.DirectoryName + "\" + $file.BaseName + ".pdf"
    $presentation.SaveAs($pdfPath, 32) # 32 is the enum for PDF format
    $presentation.Close()
}

# Get all Word, Excel, and PowerPoint files in the directory
$files = Get-ChildItem $directory -Recurse | Where-Object {
    $_.Extension -match "\.(docx?|xlsx?|pptx?)$"
}

# Process each file based on its type
foreach ($file in $files) {
    switch ($file.Extension) {
        ".doc", ".docx" { Convert-WordToPDF $file }
        ".xls", ".xlsx" { Convert-ExcelToPDF $file }
        ".ppt", ".pptx" { Convert-PowerPointToPDF $file }
    }
}

# Quit the applications
$word.Quit()
$excel.Quit()
$powerPoint.Quit()

# Release COM objects
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($powerPoint) | Out-Null
