def isPhoneNumber(text):
   if len(text) != 12:
         return False
     for i in range(0, 3):
     
        if not text[i].isdecimal():
             return False
             
    if text[3] != '-':
         return False
     for i in range(4, 7):
        if not text[i].isdecimal():
             return False
             
    if text[7] != '-':
         return False
     for i in range(8, 12):
        if not text[i].isdecimal():
             return False
    return True

print('Is 776-890-1721 a phone number?')
print(isPhoneNumber('776-890-1721'))
print('Is  a phone number?')
print(isPhoneNumber('Moshi moshi'))
