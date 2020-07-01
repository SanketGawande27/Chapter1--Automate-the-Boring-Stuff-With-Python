from pathlib import Path 
p = Path('readwritefile.txt')
p.write_text('Hello, I am Sanket .... How are you ....??')
rd = p.read_text()
print(rd)
