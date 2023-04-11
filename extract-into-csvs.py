# -----------Ain Salleh-----------------
# This code is used to extract every sheet
# from a single Excel file into individual CSVs.
# You will be prompted to enter the name of the excel file
# and you must include .xlsx . Example: Sample_1.xlsx
# --------------------------------------

import pandas as pd
import openpyxl

# Use the `input` function to get user input for the file name
excelname = input("Enter your excel name (E.g Sample_1.xlsx) = ")

try:
    # Read all sheets from the Excel file into a dictionary of dataframes
    dfs = pd.read_excel(excelname, sheet_name=None)

    # Loop through each sheet name and corresponding data, and save to a CSV file
    for sheet_name, data in dfs.items():
        data.to_csv(f"{sheet_name}.csv", index=False)

    # Print a success message
    print("CSV files created successfully!")
    
except Exception as e:
    # Print an error message with the specific error that occurred
    print(f"An error occurred: {e}")
