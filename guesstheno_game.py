    #Guess the number game.
import random
secretnumber=random.randint(1,10)
print('I am thinking of a number between 1 and 10')

for guesstaken in range(1,4):
   print('Take a guess')
   guess=int(input())
 
  if guess < secretnumber:
       print('your guess is too low')
   elif guess > secretnumber:
       print('your guess is to heigh')
    else:
       break
   
   if guess == secretnumber:
       print('Good Job ! you win '+str(guesstaken) +'guesses!')
   else:
       print('Nope .. the number I was thinking of was '+str(secretnumber))
