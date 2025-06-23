# Code to open Excel file in each sub folder and paste the csv data into it at the specified worksheet location.

import os
import openpyxl
import csv

def update_excel_sheets(root_folder):
    for foldername, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".xlsx"):
                file_path = os.path.join(foldername, filename)
                try:
                    workbook = openpyxl.load_workbook(file_path)
                    sheet = workbook["Sheet2"]      # The name of the worksheet where we want to paste the data
                    csv_file_path = "csvfile.csv"      # The csv file in which our raw data is present.
                    with open(csv_file_path, "r") as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)
                        
                        for row in csv_reader:
                            sheet.append(row)

                    workbook.save(file_path)     
                    print(f"Updated {filename} in {foldername} with data from CSV")  
                except Exception as e:
                    print(f"Error Updating {filename} in {foldername}: {e}")
                    
update_excel_sheets('Root_folder')          # This is the path for main folder or the Root Folder.
