#finding elements with select() method


import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems[0])) 
pp=elems[0].getText()
print(pp)
ppp=elems[0].attrs
print(ppp)
pElems = exampleSoup.select('p')
print(str(pElems[0]))
temp=pElems[0].getText()
print(temp)
