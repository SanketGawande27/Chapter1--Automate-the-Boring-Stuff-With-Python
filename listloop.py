catname=[]
while True:
   print('Enter your cat name :')
   name=input()
   
   if name =='':
    break
      
   catname=catname+[name]
print('Cat names are :')
for name in catname:
    print(''+name)
 
 
  
