import openpyxl
import os
import time

location = os.getcwd()

print(location)

file = "C:\\Users\\Megha Kadam\\PycharmProjects\\pythonProject\\TestData\\test100.xlsx"

workbook = openpyxl.load_workbook(file)
sheet = workbook["Sheet1"]
# sheet = workbook.active

for r in range(1,5):
    for c in range(1,3):
        print(sheet.cell(row=r,column=c).value,end = " ")
    print()
