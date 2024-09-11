import os
import csv
import chardet
import logging
from datetime import datetime

# ログ設定
logging.basicConfig(filename='file_processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def detect_encoding(file_path):
    """
    ファイルのエンコーディングを自動検出する関数。
    """
    try:
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            return result['encoding']
    except Exception as e:
        logging.error(f"ファイルのエンコーディング検出中にエラー: {e}")
        return None

def check_words_in_file(file_path, word1_list, word2_list):
    """
    指定されたファイル内にword1_listやword2_listの単語が1つでも含まれるかどうかを確認する関数。
    """
    matched_words = []  # マッチした単語を保存するリスト
    try:
        # ファイルのエンコーディングを検出
        encoding = detect_encoding(file_path)
        if not encoding:
            return False, [], f"エンコーディングを検出できませんでした: {file_path}"

        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
            # word1_listやword2_listのいずれかの単語が含まれているかをチェック
            for word1 in word1_list:
                if word1 in content:
                    matched_words.append(word1)

            for word2 in word2_list:
                if word2 in content:
                    matched_words.append(word2)

            return len(matched_words) > 0, matched_words, None
    except Exception as e:
        logging.error(f"ファイル {file_path} の処理中にエラーが発生しました: {e}")
        return False, [], str(e)


def process_file_paths(input_file, word1_list, word2_list, output_file=None):
    """
    ファイルパスを読み込み、各ファイル内に指定された単語が含まれるかを検査し、
    結果をCSVに出力し、ログを記録する。
    """
    results = []

    # 入力ファイルがCSVかテキストかを判断して読み込む
    try:
        with open(input_file, 'rb') as f:
            # 入力ファイルのエンコーディングを自動判定
            raw_data = f.read()
            detected = chardet.detect(raw_data)
            encoding = detected['encoding']
        
        # エンコーディングを用いて再度ファイルを開く
        with open(input_file, 'r', encoding=encoding) as f:
            if input_file.endswith('.csv'):
                reader = csv.reader(f)
                file_paths = [row[0] for row in reader]
            else:
                file_paths = [line.strip() for line in f.readlines()]
    except Exception as e:
        logging.error(f"入力ファイル {input_file} の読み込み中にエラーが発生しました: {e}")
        return

    # 各ファイルパスについて単語のチェックを実施
    for file_path in file_paths:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if os.path.exists(file_path):
            logging.info(f"ファイル {file_path} の処理を開始")
            status, matched_words, error_message = check_words_in_file(file_path, word1_list, word2_list)
            status_text = "成功" if status else "失敗"
            matched_str = ','.join(matched_words) if matched_words else 'なし'
            results.append([timestamp, file_path, status_text, matched_str, error_message or ''])
            logging.info(f"ファイル {file_path} の処理結果: {status_text}, マッチ: {matched_str}")
        else:
            error_message = f"ファイルが存在しません: {file_path}"
            logging.error(error_message)
            results.append([timestamp, file_path, "失敗", 'なし', error_message])

    # 結果をCSVに出力
    if output_file:
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'File Path', 'Status', 'Matched', 'Error Message'])
                writer.writerows(results)
            logging.info(f"結果が {output_file} に出力されました。")
        except Exception as e:
            logging.error(f"出力ファイル {output_file} の作成中にエラーが発生しました: {e}")
    else:
        # 標準出力に結果を表示
        print("ファイルパスと検索結果:")
        for result in results:
            print(result)

# 使い方
input_file = 'file_paths.csv'  # または 'file_paths.txt'
word1_list = ['ワード1', 'ワード1の別名']  # 複数の単語を含むリスト
word2_list = ['ワード2', 'ワード2の別名']  # 複数の単語を含むリスト
output_file = 'results.csv'  # 結果をCSVに出力する場合。不要ならNoneにする。

process_file_paths(input_file, word1_list, word2_list, output_file)
