Option Explicit

' This script extracts multiple ZIP files listed in a worksheet using 7-Zip.
' It assumes that the worksheet "Sheet1" contains a list of ZIP file paths, passwords, and destination folders starting from row 2.
' The results of each extraction attempt are logged in the worksheet.

Sub ExtractMultipleZipFiles()
    ' Define variables for the worksheet and range
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1")
    
    ' Define variables for loop and data processing
    Dim i As Long
    Dim LastRow As Long
    Dim DataRange As Variant
    
    ' Determine the last row with data in column A
    LastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    
    ' Load all relevant data into a two-dimensional array for faster processing
    If LastRow >= 2 Then
        DataRange = ws.Range("A2:C" & LastRow).Value
    Else
        MsgBox "No data found.", vbExclamation
        Exit Sub
    End If
    
    ' Define variables for 7-Zip command execution
    Dim PathTo7Zip As String
    PathTo7Zip = """C:\Program Files\7-Zip\7z.exe"""
    
    Dim ShellApp As Object
    Set ShellApp = CreateObject("WScript.Shell")
    
    Dim ShellCommand As String
    Dim ExecutionResult As Integer
    
    ' Process each row in the array
    For i = LBound(DataRange, 1) To UBound(DataRange, 1)
        ' Prepare the command for extracting the ZIP file
        ShellCommand = PathTo7Zip & " x -p" & DataRange(i, 2) & " """ & DataRange(i, 1) & """ -o""" & DataRange(i, 3) & """ -aoa"
        
        ' Execute the command
        ExecutionResult = ShellApp.Run(ShellCommand, 0, True)
        
        ' Log the result back into the worksheet
        If ExecutionResult = 0 Then
            ws.Cells(i + 1, 4).Value = "Success"
        Else
            ws.Cells(i + 1, 4).Value = "Failure"
        End If
    Next i
    
    ' Cleanup
    Set ShellApp = Nothing
    MsgBox "Process completed.", vbInformation
End Sub
