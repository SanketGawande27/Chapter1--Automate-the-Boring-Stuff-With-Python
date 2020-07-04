#write Objects 

import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
frow=outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
print(frow)
secrow=outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
print(secrow)
thrrowoutputWriter.writerow([1, 2, 3.141592, 4])
print(thrrow)
outputFile.close()
