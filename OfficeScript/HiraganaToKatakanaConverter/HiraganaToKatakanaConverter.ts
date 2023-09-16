// 正規表現を使用して、文字列内のひらがな文字をカタカナに変換する
function main(workbook: ExcelScript.Workbook, str: string) {
    return str.replace(/[\u3041-\u3096]/g, ch =>
        // 文字コードを変換して、カタカナ文字にマッピング
        String.fromCharCode(ch.charCodeAt(0) + 0x60)
    );
}
