Attribute VB_Name = "CreateFoldersBySelectionValue"
Option Explicit

' Project Name    : Create Folders Based on Selected Cell Values Under the Chosen Folder
' File Name       : CreateFoldersBySelectionValue.bas
' Feature         : Easily create folders based on selected cell values. Includes error handling.
' Creation Date   : 2022-05-04
' Programming Language Used:
'' Visual Basic for Applications
' Author          : DEmodoriGatsuO https://github.com/DEmodoriGatsuO
' Twitter         : https://twitter.com/DemodoriGatsuo
' Copyright (c) 2022, Tech Lovers. All rights reserved

'==================================
' createFoldersBySelectionValue Main Module
'==================================
Sub createFoldersBySelectionValue()

    '---- Constant and Variable List ----
    Const successPrompt   As String = "Everything was completed successfully" ' Prompt for successful completion
    Const successTitle    As String = "Success" ' Title for successful completion
    Dim folderPath        As String ' Path of the selected folder
    Dim data              As Variant ' Store values of selected cells in a 2D array
    Dim collectionFolders As New Collection ' Collection to hold folders to create
    Dim item              As Variant ' Iterator for the collection
    Dim errorLog          As New Collection ' Collection to log errors
    Dim errorLine         As Variant ' Line for the error log collection
    Dim i                 As Long ' Integer iterator
    Dim messageStr        As String ' String for MsgBox
    Dim logPath           As String ' Path to output the log

    '1. Open file dialog to select the folder for listing
    With Application.FileDialog(msoFileDialogFolderPicker)
        Select Case .Show
            Case True: folderPath = .SelectedItems(1)
            Case False: Exit Sub
        End Select
    End With

    '2. Store values of selected cells in "data"
    data = Selection.Value

    '3. Populate "collectionFolders" with values from the 2D array
    ' Exclude empty cells that are not intended for creation
    Select Case IsArray(data)
        Case False
            If data = "" Then Exit Sub
            ' Add the value of the selected cell to the collection
            collectionFolders.Add data
        Case True
            ' Add all non-empty cell values to the collection
            For Each item In data
                If item <> "" Then collectionFolders.Add item
            Next item
    End Select

    '4. Iterate through collection items and create folders
    ' Ignore errors (e.g., invalid characters or duplicate folder names)
    For Each item In collectionFolders
        On Error Resume Next
        MkDir folderPath & "\" & item
        If Err.Number <> 0 Then
            errorLine = Array(item, Err.Number, Err.Description)
            errorLog.Add errorLine
            Err.Clear
        End If
    Next item

    '5. If there are no errors, display a message box and exit
    If errorLog.Count = 0 Then
        MsgBox successPrompt, vbInformation, successTitle
        Exit Sub
    End If

    '!! If errors exist !!
    If errorLog.Count <> 0 Then
        ' Convert errorLog items (arrays with 3 elements) to strings and concatenate them to messageStr
        For i = 1 To errorLog.Count
            Select Case i
                Case 1 ' Set title for the first index
                    messageStr = "Error Log" & vbCrLf & Join(errorLog(i), " ") & vbCrLf
                Case errorLog.Count  ' Set total count for the last index
                    messageStr = messageStr & Join(errorLog(i), " ") & vbCrLf & errorLog.Count & " errors"
                Case Else
                    messageStr = messageStr & Join(errorLog(i), " ") & vbCrLf
            End Select
        Next i
    End If

    '' Set the output path to the folder where this VBA file is bound, and format the log file name using the Now function to prevent duplicates
    logPath = ThisWorkbook.Path & "\" & Format(Now(), "yyyymmddhhmmss") & "error_log.txt"
    
    '' ☆ Jump to Private Sub - This is a technique for writing to a text file and displaying it using a shell!
    Call outputTextFile(logPath, messageStr)

End Sub

'==================================
' Tips: Output String to Text File
' Arguments: targetPath (path to the file), txt (text to write)
'==================================
Private Sub outputTextFile(targetPath, txt)
    ' Use CreateObject instead of references to prevent issues
    Dim wsh
    Set wsh = CreateObject("Wscript.Shell")
    
    ' Prepare to run the shell
    Dim fileNumber As Integer
    fileNumber = FreeFile
    
    ' Write to the text file in overwrite mode (create if doesn't exist)
    Open targetPath For Output As #fileNumber
        Print #fileNumber, txt
    Close #fileNumber
    
    ' Display the text file on top
    wsh.Run targetPath, 3
    Set wsh = Nothing
    
End Sub
