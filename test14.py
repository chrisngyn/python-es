# Reading Excel sheets in Python - this Python program uses "sales.xlsx"
# This uses the Python module "pandas" and "xlrd", so we run: python3 -m pip install pandas, then xlrd.

import pandas as pd

file = pd.ExcelFile("sales.xlsx")
print(file.sheet_names)             # prints a list of the two sheet names in our Excel file

sheet = file.parse("sales")
print(type(sheet))
print("")
print(sheet)                        # print entire sheet
print("")
print(sheet.Date)                   # print column from sheet
print("")
print(sheet.Amount.sum())           # aggregate the column
print("")
print(sheet.loc[0])                 # print first row from that column
print("")
print(sheet.loc[0, "Amount"])       # from the first row, print only the Amount column value
print("")
sheet.set_index("Customer", inplace=True)       # searching by index
print(sheet.loc["MMC Inc."])                    # getting all sales made to MMC Inc.
print("")
sheet = sheet.reset_index()         # reset the index so now it's not locked anymore
print("")
print(sheet.loc[ sheet["Invoice"] == 99 ])      # searching by Series, in a DataFrame. Series is a column in a DataFrame
print("")
print(sheet.loc[ sheet["Amount"] > 2000 ])
print("")
print(sheet.loc[ sheet["Amount"].idxmax() ])
print("")
print(sheet.loc[ sheet["Amount"].idxmax() ])["Customer"]    # grabbing specific column from that dataframe
print("")
print(sheet.loc[ sheet["Amount"] > 1500 ]["Customer"].unique())     # unique Customer values from this query

# TL;DR - LOTS OF THINGS YOU CAN DO WITH MODULE PANDAS AND XLRD.