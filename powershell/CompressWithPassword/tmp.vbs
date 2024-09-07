' HTMLファイルとPDFファイルのパス
Dim htmlFilePath
Dim pdfFilePath
htmlFilePath = "C:\path\to\your\file.html"
pdfFilePath = "C:\path\to\output\file.pdf"

' Wordオブジェクトの作成
Dim wordApp
Set wordApp = CreateObject("Word.Application")

' Wordの表示を抑制
wordApp.Visible = False

' HTMLファイルを開く
Dim doc
Set doc = wordApp.Documents.Open(htmlFilePath)

' PDFとして保存
doc.SaveAs2 pdfFilePath, 17 ' 17 は PDF 形式を意味します

' ドキュメントを閉じる
doc.Close

' Word アプリケーションを閉じる
wordApp.Quit

' オブジェクトの解放
Set doc = Nothing
Set wordApp = Nothing

WScript.Echo "PDFファイルが作成されました: " & pdfFilePath
