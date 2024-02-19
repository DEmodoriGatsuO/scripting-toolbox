' This script reads a CSV file containing paths to ZIP files, their corresponding passwords, and destination folders.
' It uses 7-Zip to extract each ZIP file to the specified destination using the given password.
' The result of each operation (success or failure) is written to a new CSV file.

' Create the FileSystemObject to work with files
Dim objFSO
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Create the Shell object to run commands
Dim objShell
Set objShell = CreateObject("WScript.Shell")

' Specify the path to the input CSV file
Dim strInputCSV
strInputCSV = "C:\Users\input.csv"

' Specify the path to the output CSV file
Dim strOutputCSV
strOutputCSV = "C:\Users\output.csv"

' Open the input CSV file for reading
Dim objTextFile
Set objTextFile = objFSO.OpenTextFile(strInputCSV, 1)

' Create the output CSV file for writing results
Dim objOutputFile
Set objOutputFile = objFSO.CreateTextFile(strOutputCSV, True)

' Process each line in the input file
Dim strLine
Dim arrData
Dim strCommand
Dim intResult

' Read and process each line until the end of the file
Do Until objTextFile.AtEndOfStream
    strLine = objTextFile.ReadLine
    arrData = Split(strLine, ",") ' Split the line into components

    ' Construct the command to execute using 7-Zip
    strCommand = """C:\Program Files\7-Zip\7z.exe"" x -p" & arrData(1) & " """ & arrData(0) & """ -o""" & arrData(2) & """ -aoa"

    ' Execute the command and wait for it to complete
    intResult = objShell.Run(strCommand, 0, True)

    ' Write the result of the operation to the output file
    If intResult = 0 Then
        objOutputFile.WriteLine Join(arrData, ",") & ",Success"
    Else
        objOutputFile.WriteLine Join(arrData, ",") & ",Failure"
    End If
Loop

' Close the input and output files
objTextFile.Close
objOutputFile.Close

' Release the objects
Set objTextFile = Nothing
Set objOutputFile = Nothing
Set objFSO = Nothing
Set objShell = Nothing