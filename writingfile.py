tempFile = open('readfile.txt', 'w')
tempFile.write('Hello, Iam Sanket ....\n')
tempFile.close()
tempFile = open('readfile.txt', 'a')
tempFile.write('Nice to meet you again ..... !\nhave a wonderfull day......')
tempFile.close()
tempFile = open('readfile.txt')
fullcontent = tempFile.read()
tempFile.close()
print(fullcontent)





 Updates were rejected because the remote contains work that you do not have locally. This is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes

