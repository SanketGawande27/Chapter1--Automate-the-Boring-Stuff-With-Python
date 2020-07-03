#reading PDF


import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageno=pdfReader.numPages
print(pageno)
pageObj = pdfReader.getPage(0)
totaltext=pageObj.extractText()
print(totaltext)
