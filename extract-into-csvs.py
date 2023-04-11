# -----------Ain Salleh-----------------
# This code is used to extract every sheet
# from a single Excel file into individual CSVs.
# You will be prompted to enter the name of the excel file
# and you must include .xlsx . Example: Sample_1.xlsx
# --------------------------------------

import pandas as pd
import sys

excelname = input("Enter your excel name (E.g Sample_1.xlsx) = ")

try:
  dfs = pd.read_excel(excelname, sheet_name=None)
  for sheet_name, data in dfs.items():
      data.to_csv(f"{sheet_name}.csv", index=False)
except:
  print("An error occurred")
