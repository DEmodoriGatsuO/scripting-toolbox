Get-ChildItem -Directory | Select-Object Name, FullName | Export-Csv -Path "folderlist.csv" -NoTypeInformation
