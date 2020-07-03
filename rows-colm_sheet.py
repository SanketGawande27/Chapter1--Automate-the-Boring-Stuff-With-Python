#geting rows and columns from sheet

import openpyxl
 wb = openpyxl.load_workbook('example.xlsx')
 sheet = wb['Sheet1']
 tuple(sheet['A1':'C3']) # Get all cells from A1 to C3.
   ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))
  for rowOfCellObjects in sheet['A1':'C3']:
      for cellObj in rowOfCellObjects:
          print(cellObj.coordinate, cellObj.value)
          print('--- END OF ROW ---')
