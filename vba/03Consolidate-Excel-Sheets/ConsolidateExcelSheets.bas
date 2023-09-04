Attribute VB_Name = "ConsolidateExcelSheets"
Option Explicit

' Script Name     : ConsolidateExcelSheets
' Description     : Consolidates all worksheets from Excel files in a selected folder into a single workbook.
' File Name       : ConsolidateExcelSheets.bas
' Created Date    : 2022-05-03
' Programming Language: Visual Basic for Applications
' Author          : DEmodoriGatsuO https://github.com/DEmodoriGatsuO
' Twitter         : https://twitter.com/DemodoriGatsuo

Sub ConsolidateExcelSheets()

    ' Constants and variables
    Const FILE_EXTENSION As String = "\*.xls*" ' Excel file extension
    Dim fileCollection As New Collection     ' Collection to store file paths temporarily
    Dim filePath As String                  ' File path
    Dim fileName As String                  ' File name
    Const SUMMARY_SHEET_NAME As String = "contents" ' Name of the summary sheet
    Dim newWorkbook As Workbook              ' New workbook to consolidate sheets
    Dim newWorksheet As Worksheet            ' Current sheet in new workbook
    Dim worksheetCounter As Long             ' Count of worksheets
    Dim headerRow As Variant: headerRow = Array("FilePath", "FileName", "SheetName") ' Header row for the summary sheet
    Dim rowIndex As Long                    ' Index for the first dimension of the array
    Dim columnIndex As Long                 ' Index for the second dimension of the array
    
    ' 1. Select the folder containing Excel files using a file dialog
    With Application.FileDialog(msoFileDialogFolderPicker)
        Select Case .Show
            Case True: filePath = .SelectedItems(1)
            Case False: Exit Sub
        End Select
    End With

    ' 2. Check if files with the specified extension exist in the selected folder
    fileName = Dir(filePath & FILE_EXTENSION)
    If fileName = "" Then
        MsgBox "No files found in the selected folder.", vbCritical, "Error"
        Exit Sub
    End If
    
    ' 3. Create header row for the summary sheet
    fileCollection.Add headerRow
    
    ' 4. Add files found using Dir() to the collection
    Do While fileName <> ""
        fileCollection.Add Array((filePath & "\" & fileName), fileName)
        fileName = Dir()
    Loop
    
    ' Enable error handling
    On Error Resume Next
    
    ' Disable alerts and optimization settings for faster processing
    With Application
        .DisplayAlerts = False
        .ScreenUpdating = False
        .EnableEvents = False
    End With
    
    ' Create a new workbook for consolidation
    Set newWorkbook = Workbooks.Add
    Set newWorksheet = newWorkbook.Sheets(1)
    newWorksheet.Name = SUMMARY_SHEET_NAME
    
    ' Prepare the collection for storing details of worksheets
    worksheetCounter = Worksheets.Count
    fileCollection.Add headerRow
    rowIndex = 0
    
    ' Iterate through the files in the collection
    For i = 2 To fileCollection.Count
        ' Create an array [ FullPath FileName SheetName ]
        headerRow = Array(fileCollection(i)(0), Dir(fileCollection(i)(0)), "SheetName")
        
        ' Open the Excel file
        Workbooks.Open Filename:=headerRow(0)
        
        ' Iterate through worksheets in the opened workbook
        For Each newWorksheet In Workbooks(headerRow(1)).Worksheets
            ' Update sheet name in the array
            headerRow(2) = newWorksheet.Name
            
            ' Copy the current worksheet to the consolidated workbook
            newWorksheet.Copy After:=newWorkbook.Sheets(worksheetCounter)
            worksheetCounter = worksheetCounter + 1
            
            ' Add the array to the collection
            fileCollection.Add headerRow
        Next newWorksheet
        
        ' Close the opened workbook without saving
        Workbooks(headerRow(1)).Close SaveChanges:=False
    Next i
    
    ' Enable alerts
    Application.DisplayAlerts = True
    
    ' Convert the collection to a two-dimensional array
    Dim dataArr() As Variant
    ReDim dataArr(fileCollection.Count, LBound(fileCollection(1)) To UBound(fileCollection(1)))
    
    ' Populate the array
    For Each headerRow In fileCollection
        For columnIndex = LBound(headerRow) To UBound(headerRow)
            dataArr(rowIndex, columnIndex) = headerRow(columnIndex)
        Next columnIndex
        rowIndex = rowIndex + 1
    Next headerRow
    
    ' Populate the summary sheet with the array
    With newWorkbook.Sheets(SUMMARY_SHEET_NAME)
        .Range(.Cells(1, 1), .Cells(UBound(dataArr, 1) + 1, UBound(dataArr, 2) + 1)) = dataArr
        .Range(.Cells(1, 1), .Cells(UBound(dataArr, 1) + 1, UBound(dataArr, 2) + 1)).Columns.AutoFit
        .Activate
    End With
    
    ' Re-enable screen updating and events
    With Application
        .ScreenUpdating = True
        .EnableEvents = True
    End With
    
    ' Display completion message
    MsgBox newWorkbook.Name & vbNewLine & "Consolidated sheets from Excel files in the selected folder!", vbInformation, "Success"
    
    ' Release object variables
    Set newWorkbook = Nothing

End Sub
