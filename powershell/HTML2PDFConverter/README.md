# HTML to PDF Converter

このツールは、HTMLファイルをPDFに変換するための簡単なスクリプトです。PowerShellとMicrosoft Wordを使用して、HTMLファイルをPDFファイルに変換します。

## 前提条件

- Microsoft Windows OS
- Microsoft Wordがインストールされていること
- PowerShellが利用可能であること

## セットアップ

1. `ConvertToPDF.ps1` という名前のPowerShellスクリプトを任意のディレクトリに保存します。
2. `HTMLToPDF.bat` という名前のバッチファイルを同じディレクトリに保存します。

## 使用方法

1. `HTMLToPDF.bat` ファイルにHTMLファイルをドラッグアンドドロップします。
2. 同じディレクトリにPDFファイルが生成されます。

## スクリプトの詳細

- `ConvertToPDF.ps1`: このPowerShellスクリプトは、指定されたHTMLファイルをPDFに変換します。WordのCOMオブジェクトを使用してHTMLファイルを開き、PDFとして保存します。
- `HTMLToPDF.bat`: このバッチファイルは、ドラッグアンドドロップされたHTMLファイルを`ConvertToPDF.ps1` スクリプトに渡します。

## 注意事項

- このツールは、Microsoft WordがインストールされているWindows環境でのみ動作します。
- 大量のファイルを一度に変換する際には、システムのパフォーマンスに影響を与える可能性があります。
- セキュリティ設定によっては、スクリプトの実行を許可するためにPowerShellの実行ポリシーを変更する必要があるかもしれません。
- Create by chatgpt
