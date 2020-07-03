#create spreadsheet

import ezsheets
ss = ezsheets.createSpreadsheet('Title of My New Spreadsheet')
sstitle=ss.title
print(sstitle)
