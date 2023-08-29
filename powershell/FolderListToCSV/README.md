# FolderListToCSV.ps1 スクリプト解説

このスクリプトは、特定のフォルダ内のサブフォルダとファイルの一覧を再帰的に取得し、その情報をCSVファイルに出力するためのものです。

## 出力形式

以下の列がCSVファイルに出力されます:

- FullPath: ファイルまたはフォルダのフルパス
- SubfolderName: ファイルを含むサブフォルダの名前
- FileName: ファイル名
- Extension: ファイルの拡張子

## 使用方法

1. `folderPath` 変数に、一覧を取得したいフォルダのパスを設定します。
2. `csvPath` 変数に、CSVファイルの出力先パスを設定します。
3. スクリプトを実行します。

**注意:** フォルダやファイルへのアクセス権限を持っていることを確認してください。

```powershell
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
$data | Export-Csv -Path $csvPath -NoTypeInformation
```

