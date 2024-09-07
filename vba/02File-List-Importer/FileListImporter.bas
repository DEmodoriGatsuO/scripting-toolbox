Attribute VB_Name = "FileListImporter"
Option Explicit
'=============================================================================
' Project Name    : File List Importer
' Module Name     : FileListImporter.bas
' Feature         : Imports a list of selected files into Excel using a file dialog
' Creation Date   : 2022.05.02
' Programming Language: Visual Basic for Applications (VBA)
' Author          : DEmodoriGatsuO (https://github.com/DEmodoriGatsuO)
' Twitter         : https://twitter.com/DemodoriGatsuo
' Copyright (c) 2022, Tech Lovers. All rights reserved.
'=============================================================================

'==================================
' FileListImporter Main Module
'==================================
Sub ImportFileList()
    ' Constants and Variables
    Const FILE_EXTENSION As String = "\*.*" ' File extension
    Dim fileCollection   As New Collection  ' Collection to store full file paths
    Dim folderPath       As String          ' Folder path selected using file dialog
    Dim fileName         As String          ' Current file name
    Dim headerRow        As Variant: headerRow = Array("FullPath", "Filename") ' Header
    Dim item             As Variant         ' Collection iterator
    Dim rowIndex         As Long            ' Row index for array
    Dim colIndex         As Long            ' Column index for array
    
    ' 1. Open the file dialog to select the folder for listing files
    With Application.FileDialog(msoFileDialogFolderPicker)
        Select Case .Show
            Case True: folderPath = .SelectedItems(1)
            Case False: Exit Sub
        End Select
    End With
    
    ' 2. Check if there are any files in the selected folder
    fileName = Dir(folderPath & FILE_EXTENSION)
    If fileName = "" Then
        MsgBox "No files found in the selected folder", vbCritical, "Error"
        Exit Sub
    End If
    
    ' 3. Add header row to collection and initial file entry
    fileCollection.Add headerRow
    fileCollection.Add Array((folderPath & "\" & fileName), fileName)
    
    ' 4. Add files to the collection using Dir() function
    Do While fileName <> ""
        fileName = Dir()
        If fileName <> "" Then fileCollection.Add Array((folderPath & "\" & fileName), fileName)
    Loop
    
    ' 5. Convert collection to a two-dimensional array
    Dim fileListArray() As Variant
    ReDim fileListArray(fileCollection.Count, LBound(fileCollection(1)) To UBound(fileCollection(1)))
    
    ' 6. Populate the array
    rowIndex = 0
    For Each item In fileCollection
        For colIndex = LBound(item) To UBound(item)
            fileListArray(rowIndex, colIndex) = item(colIndex)
        Next colIndex
        rowIndex = rowIndex + 1
    Next item
    
    ' 7. Output the array to the active worksheet, starting from the active cell
    Dim activeCell As Range
    Set activeCell = ActiveCell
    activeCell.Resize(UBound(fileListArray, 1) + 1, UBound(fileListArray, 2) + 1).Value = fileListArray
    
    ' 8. Display completion message
    MsgBox folderPath & vbNewLine & "File list has been imported.", vbInformation, "Success"
End Sub
