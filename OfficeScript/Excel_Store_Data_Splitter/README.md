# Excel Script for Splitting Data by Unique Store Names

## 概要
このスクリプトは、指定された開始セル（C1セルの値を使用）からC列にある店舗名を取得し、重複を削除してユニークな店舗ごとに新しいシートを作成し、店舗別の結果を挿入します。C1セルの値を変更することで動的に対応可能です。

## ファイル構成
- `main.ts`: メインのExcelスクリプトファイル。以下の関数を含みます。
  - `main(workbook: ExcelScript.Workbook)`: 指定された開始セルからC列のデータを取得し、各ユニークな店舗ごとに新しいシートを作成してデータを挿入します。

## 使い方
1. **スクリプトの追加**:
   - Excelの「Automate」タブを開き、「スクリプトの作成」をクリックします。
   - `main.ts`の内容をコピーして、Excelスクリプトエディタに貼り付けます。
   - スクリプトに適切な名前を付けて保存します。

2. **C1セルの設定**:
   - C1セルに開始セルのアドレス（例：C2）を文字列として入力します。

3. **スクリプトの実行**:
   - 保存したスクリプトを実行します。

## スクリプトの説明
```typescript
/**
 * 作成者: ChatGPT
 * 関数の目的: 指定された開始セル（C1セルの値を使用）からC列にある店舗名を取得し、
 *              重複を削除してユニークな店舗ごとに新しいシートを作成し、店舗別の結果を挿入する。
 */

function main(workbook: ExcelScript.Workbook) {
  // C1セルの値を文字列の定数として設定
  const startCellAddress: string = "C1";
  
  // アクティブなシートを取得
  const sheet: ExcelScript.Worksheet = workbook.getActiveWorksheet();
  
  // C1セルの値を開始セルとして取得（C1の値を変更することで動的に対応可能）
  const startCell: ExcelScript.Range = sheet.getRange(startCellAddress);
  
  // シートの使用範囲を取得
  const usedRange: ExcelScript.Range = sheet.getUsedRange();
  
  // 開始行と終了行のインデックスを取得
  const startRow: number = startCell.getRowIndex();
  const endRow: number = usedRange.getRowCount() - 1;
  
  // 開始セルの列インデックスを取得
  const column: number = startCell.getColumnIndex();
  
  // C列のデータを格納するための配列を初期化
  const storeData: string[] = [];
  
  // C列のデータをループで取得
  for (let i = startRow; i <= endRow; i++) {
    const cellValue: string = sheet.getCell(i, column).getValue() as string;
    if (cellValue) {
      storeData.push(cellValue); // 値が存在する場合のみ配列に追加
    }
  }

  // 重複を削除してユニークな店舗名の配列を作成
  const uniqueStores: string[] = Array.from(new Set(storeData));
  
  // 各店舗ごとに新しいシートを作成しデータを挿入
  uniqueStores.forEach(store => {
    // 店舗名に対応するシートを取得（存在しない場合は新規作成）
    let storeSheet: ExcelScript.Worksheet = workbook.getWorksheet(store);
    if (!storeSheet) {
      storeSheet = workbook.addWorksheet(store); // 新しいシートを作成
    } else {
      storeSheet.getUsedRange()?.clear(); // 既存のデータをクリア
    }
    
    // 元のシートから店舗データを抽出して配列に追加
    const storeRows: (string | number | boolean)[][] = [];
    for (let i = startRow; i <= endRow; i++) {
      const cellValue: string = sheet.getCell(i, column).getValue() as string;
      if (cellValue === store) {
        storeRows.push(sheet.getRow(i).getValues()[0] as (string | number | boolean)[]); // 行データを配列に追加
      }
    }
    
    // 店舗ごとのシートにデータを挿入
    if (storeRows.length > 0) {
      storeSheet.getRangeByIndexes(0, 0, storeRows.length, storeRows[0].length).setValues(storeRows);
    }
  });
}
```

## 注意点
- このスクリプトは、C1セルに開始セルのアドレスが正しく設定されていることを前提としています。
- スクリプトの実行により既存のデータがクリアされるため、重要なデータはバックアップを取ってください。

## ライセンス
このプロジェクトは、MITライセンスのもとで提供されています。詳細はLICENSEファイルを参照してください。
