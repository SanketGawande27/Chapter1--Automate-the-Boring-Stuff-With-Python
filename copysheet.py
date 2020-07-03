##copy sheets


import ezsheets
ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
ss1[0].copyTo(ss2)  
sss=ss2.sheetTitles    
print(sss)
