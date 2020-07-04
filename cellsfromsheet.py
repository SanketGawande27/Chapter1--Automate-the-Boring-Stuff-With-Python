#get cells of sheet 


import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1'] # Get a sheet from the workbook.
s1=sheet['A1'] # Get a cell from the sheet.
print(s1)
s2=sheet['A1'].value # Get the value from the cell.
datetime.datetime(2015, 4, 5, 13, 34, 2)
c = sheet['B1'] # Get another cell from the sheet.
s3=c.value
print(s3)
'Row %s, Column %s is %s' % (c.row, c.column, c.value) 'Row 1, Column B is Apples'
'Cell %s is %s' % (c.coordinate, c.value) 'Cell B1 is Apples'
s4=sheet['C1'].value
print(s4)
