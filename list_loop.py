catname = []
while True:
 print('Enter cat name '+ str(len(catname)+1))
 name = input()
if name =='':
 break  
catname = catname+[name]
print('Cat names are :')
for name in catname:
 print('  '+name) 
