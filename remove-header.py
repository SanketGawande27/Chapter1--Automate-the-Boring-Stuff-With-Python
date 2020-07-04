#Removind Header

import csv, os
os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for example1 in os.listdir('.'):
     if not example1.endswith('.csv'):
        continue    # skip non-csv files

     print('Removing header from ' + example1 + '...')
     
      # Read the CSV file in (skipping first row).
     csvRows = []
     csvFileObj = open(example1)
     readerObj = csv.reader(csvFileObj)
     for row in readerObj:
      if readerObj.line_num == 1:
          continue    # skip first row
     csvRows.append(row)
     csvFileObj.close()
     # Write out the CSV file.
     csvFileObj = open(os.path.join('headerRemoved', example1), 'w', newline='')
     csvWriter = csv.writer(csvFileObj)
     for row in csvRows:
           csvWriter.writerow(row)
     csvFileObj.close()
