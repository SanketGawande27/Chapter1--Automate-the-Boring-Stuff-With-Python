def collatz(number):
 if number%2 == 0:
  return number//2
 else:
  return 3*number+1 
  
for i in range(1,11):
 print(collatz(i))  
