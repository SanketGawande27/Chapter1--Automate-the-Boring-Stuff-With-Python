#read docx files

import docx

def getText(firstdoc):
    doc = docx.Document(firstdoc)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
    print(fullText)
