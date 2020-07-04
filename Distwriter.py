#DicTwriter

import csv
outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
a = outputDictWriter.writeheader()
print(a)
b=outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
print(b)
c=outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
print(c)
d=outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':'dog'})
print(d)
outputFile.close()
