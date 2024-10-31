# HTMLファイルのパス
$htmlFilePath = "C:\path\to\your\file.html"

# PDFファイルのパス
$pdfFilePath = "C:\path\to\output\file.pdf"

# Internet ExplorerのCOMオブジェクトを作成
$ie = New-Object -ComObject InternetExplorer.Application

try {
    # IEを非表示に設定
    $ie.Visible = $false

    # HTMLファイルを開く
    $ie.Navigate($htmlFilePath)

    # ページの読み込みを待つ
    while ($ie.Busy -eq $true) { Start-Sleep -Milliseconds 100 }

    # PDFプリンターを使って印刷
    # 注意: "Microsoft Print to PDF"のプリンター名はシステムによって異なる場合があります
    $ie.ExecWB(6,2,@($pdfFilePath,2))

    # 処理の完了を待つ
    Start-Sleep -Seconds 2
}
catch {
    Write-Host "エラー: $_"
}
finally {
    # IEを閉じる
    $ie.Quit()
}

# 結果の確認
if (Test-Path $pdfFilePath) {
    Write-Host "PDFファイルが正常に作成されました: $pdfFilePath"
} else {
    Write-Host "PDFファイルの作成に失敗しました。"
}
