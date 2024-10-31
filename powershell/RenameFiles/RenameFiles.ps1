# Set Folder Path
$folderPath = "C:\Your\Folder\Path"

# Get files
$files = Get-ChildItem -Path $folderPath

# Set variant
$oldText = "OldTextHere"
$newText = "NewTextHere"

# Replace
foreach ($file in $files) {
    $newName = $file.Name -replace $oldText, $newText
    Rename-Item -Path $file.FullName -NewName $newName
}
