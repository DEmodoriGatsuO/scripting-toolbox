Import-Csv -Path "folderlist.csv" | ForEach-Object {
  Rename-Item -Path $_.FullName -NewName $_.NewName
}
