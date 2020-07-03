#upload spreadsheets

import ezsheets
ss = ezsheets.upload('first_spreadsheet.xlsx')
up=ss.title
print(up)
