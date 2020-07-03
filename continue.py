#continus statement

while True:
 print('Who are you?')
 name = input()
 if name != 'sanket':
  continue
  print('Hello, Sanket. What is the password?')
  password = input()
 if password == 'sanket':
  break
print('Access granted.')    
