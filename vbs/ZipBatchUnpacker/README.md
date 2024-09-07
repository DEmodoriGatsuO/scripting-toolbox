# ZipBatchUnpacker

ZipBatchUnpackerは、CSVファイルを入力として使用し、複数のZIPファイルの自動展開を行うためのVBScriptプロジェクトです。CSVファイルの各行には、ZIPファイルへのパス、そのパスワード（必要な場合）、および展開先フォルダが含まれています。このスクリプトは、各エントリを処理し、ZIPファイルをそれに応じて展開し、各操作の成功または失敗を出力CSVファイルにログとして記録します。

## 特徴

- ZIPファイルのバッチ処理。
- パスワード保護されたZIPファイルに対応。
- 展開結果のログを生成。

## 前提条件

ZipBatchUnpackerを使用するには以下が必要です：

- Windowsオペレーティングシステム。
- `C:\Program Files\7-Zip\7z.exe`にアクセス可能な7-Zipがインストールされていること。
- `path_to_zip,password,destination_path`の形式でフォーマットされた入力CSVファイル。

## セットアップ

1. システムに7-Zipがインストールされていることを確認してください。
2. 必要なフォーマットで入力CSVファイルを準備してください。
3. スクリプト内の変数`strInputCSV`と`strOutputCSV`を、入力および出力CSVファイルのパスに合わせて変更してください。

## 使用方法

1. VBScriptエディタまたはメモ帳を開き、`ZipBatchUnpacker.vbs`の内容を貼り付けてください。
2. スクリプト内の`strInputCSV`および`strOutputCSV`のパスを自分の設定に合わせて変更してください。
3. スクリプトを`.vbs`拡張子で保存してください。
4. スクリプトファイルをダブルクリックして実行するか、コマンドラインから`cscript ZipBatchUnpacker.vbs`を使用して実行してください。

## 入力CSVフォーマット

入力CSVは以下のフォーマットに従う必要があります：

|Column1|Column2|Column3|
|---|---|---|
|path_to_zip_file|password|destination_folder|
|path_to_another_zip_file|another_password|another_destination_folder

注：ZIPファイルにパスワードが不要な場合は、パスワードフィールドを空にしてください。

- ヘッダーは無しにしてください

## 出力CSVフォーマット

スクリプトは、入力ファイルと同じデータを含む出力CSVファイルを生成しますが、展開の結果に基づいて各行に「Success」または「Failure」のステータスを追加します。

## ライセンス

このプロジェクトはMITライセンスの下で利用可能です。詳細についてはLICENSEファイルを参照してください。

## 免責事項

このスクリプトは「現状のまま」提供され、いかなる種類の保証も伴わないものとします。自己責任で使用してください。
