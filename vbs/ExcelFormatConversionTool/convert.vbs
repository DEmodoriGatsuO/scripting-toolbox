' Script Name: Excel File Format Converter
' Purpose: This script converts Excel files from .xls format to .xlsx format using drag-and-drop functionality.
' Author: De'modori Gatsuo
' Date: 2023-09-03

' Constants
Const XlFileFormat_xlOpenXMLWorkbook = 51 ' .xlsx: Excel Workbook

' Get the list of files passed as command line arguments (drag-and-drop).
Set args = WScript.Arguments
fileList = ""
For Each arg In args
    fileList = fileList & vbNewLine & arg
Next

' Check the arguments to ensure only .xls files are specified, exit if other types are found.
Set fobj = CreateObject("Scripting.FileSystemObject")
For Each arg In args
    ext = LCase(fobj.GetExtensionName(arg))
    If ext <> "xls" Then
        MsgBox "Only .xls files are allowed. Exiting." & vbNewLine & fileList
        WScript.Quit
    End If
Next

' Convert each specified Excel file to the latest format (.xlsx).
Set oXlsApp = CreateObject("Excel.Application")
For Each path In args
    oXlsApp.Application.Visible = True
    Set book = oXlsApp.Application.Workbooks.Open(path)
    newFilePath = Replace(path, ".xls", ".xlsx")
    book.SaveAs newFilePath, XlFileFormat_xlOpenXMLWorkbook
    book.Close
Next
oXlsApp.Quit
Set oXlsApp = Nothing

MsgBox "Conversion completed."