import time
def calcMultiplyNo():
       product = 1
       for i in range(1, 100000):
           product = product * i
       return product

startTime = time.time()
prod = calcMultiplyNo()
endTime = time.time()
  print('The result is %s digits long.' % (len(str(prod))))
  print('Took %s seconds to calculate.' % (endTime - startTime))
