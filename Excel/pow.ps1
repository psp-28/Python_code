function Update-ExcelSheets {
    param (
        [string]$rootFolder
    )

    foreach ($folder in Get-ChildItem $rootFolder -Recurse) {
        foreach ($file in $folder.GetFiles()) {
            if ($file.Extension -eq ".xlsx") {
                $filePath = $file.FullName

                try {
                    $workbook = Open-ExcelPackage $filePath
                    $sheet = $workbook.Workbook.Worksheets["Sheet2"]  # Replace "Sheet2" with the actual sheet name
                    $csvFilePath = 'csvfile.csv'  # Replace with the actual CSV file path

                    $csvData = Import-Csv $csvFilePath
                    $csvData | ForEach-Object {
                        $row = $sheet.Row($sheet.Dimension.End.Row + 1)
                        $_.PSObject.Properties.Value | ForEach-Object {
                            $cell = $row.ItemArray[$_.Name]
                            $cell.Value = $_
                        }
                    }

                    $workbook.SaveAs($filePath)
                    Write-Host "Updated $($file.Name) in $($folder.FullName) with data from CSV"
                } catch {
                    Write-Host "Error updating $($file.Name) in $($folder.FullName): $_"
                }
            }
        }
    }
}

Update-ExcelSheets -rootFolder 'Root_folder'