# base64_to_mp3_converter.py

このスクリプトは、base64文字列をデコードしてmp3ファイルに保存するためのPythonスクリプトです。

## 使い方

1. `input.txt`ファイルにデコードしたいbase64文字列を記述して保存します。
2. 以下のコマンドを実行して、デコードとmp3ファイルの保存を行います：

```bash
python base64_to_mp3_converter.py
```

3. スクリプトが実行されると、`output.mp3`という名前のファイルが生成され、デコードされたmp3ファイルが保存されます。

## スクリプトの詳細

`base64_to_mp3_converter.py`スクリプトは以下の手順で動作します：

1. `base64_file`変数で指定されたファイルからbase64文字列を読み込みます。
2. `base64_to_mp3`関数は、引数として渡されたbase64文字列をデコードして、指定された出力ファイル名（`output_file`）にmp3ファイルとして保存します。
3. デコードした結果は`output.mp3`として保存されます。

このスクリプトを利用することで、base64形式の音声データをmp3ファイルとして簡単に保存することができます。
