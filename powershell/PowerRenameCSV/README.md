# PowerRenameCSV

PowerRenameCSVはPowerShellを使用して、CSVファイルを介してフォルダ名を一括でリネームするツールです。簡単な操作で大量のフォルダの名前を効率的に変更することができます。

## 特徴

- CSVファイルを使用してリネームするフォルダのリストを簡単に管理。
- バッチファイルを使用して、非技術者でも簡単にスクリプトを実行可能。
- フォルダ名の一括変更を迅速かつ正確に行います。

## 使い方

### ステップ1: フォルダリストの準備

1. `Get-ChildItem` コマンドを使用して、対象のフォルダリストをCSVに出力します。
2. 出力されたCSVファイルに「NewName」列を追加し、リネーム後の名前を入力します。

### ステップ1: フォルダリストをCSVに書き込む

1. PowerShellを開きます。
2. 対象のフォルダが存在するディレクトリに移動します。
3. 以下のコマンドを実行して、フォルダのリストをCSVファイルに出力します。

   ```powershell
   Get-ChildItem -Directory | Select-Object Name, FullName | Export-Csv -Path "folderlist.csv" -NoTypeInformation
   ```

   これにより、現在のディレクトリにあるすべてのフォルダの名前 (`Name`) とフルパス (`FullName`) が "folderlist.csv" というファイルに保存されます。

### ステップ2: CSVファイルにリネーム列を追加

1. 生成された "folderlist.csv" ファイルをExcelなどの表計算ソフトで開きます。
2. 新しい列を追加し、「NewName」というヘッダーを設定します。
3. 各フォルダに対して新しい名前を「NewName」列に入力します。
4. 編集が完了したら、CSVファイルを保存して閉じます。

### ステップ3: PowerShellで一括リネームを実行

1. PowerShellを開きます。
1. CSVファイルを読み込み、各フォルダを新しい名前にリネームするコマンドを実行します。

```powershell
 Import-Csv -Path "folderlist.csv" | ForEach-Object {
   Rename-Item -Path $_.FullName -NewName $_.NewName
 }
```

### バッチファイルの使用

1. `RunRename.bat` バッチファイルをダブルクリックしてスクリプトを実行します。
2. スクリプトはCSVファイルを読み込み、指定された名前にフォルダを一括でリネームします。
注意点:
- リネームプロセス中にエラーが発生する可能性があります（例えば、新しい名前が既に存在する場合など）。エラーハンドリングを追加することをお勧めします。
- フォルダのリネームは元に戻せない場合があるため、実行前には十分に確認してください。
- リネームするフォルダが他のプロセスによって使用されていないことを確認してください。

```batch
@echo off
PowerShell -NoProfile -ExecutionPolicy Bypass -File "WriteCSV.ps1"
```

## 前提条件

- Windows OS
- PowerShell 5.0 以上
- CSVファイルの編集にはExcelまたは同等のソフトウェアが必要です。

## Install

このプロジェクトはインストール不要で、直接ダウンロードして使用することができます。

## Usage

PowerShellを使ってフォルダのリストをCSVに書き込み、リネームのための一括処理を行う方法をご紹介します。以下のステップに従ってください。


## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。
