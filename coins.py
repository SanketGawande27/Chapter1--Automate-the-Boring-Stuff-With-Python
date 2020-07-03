import random
numberOfStreaks = 0
for experimentNumber in range(10000):

    ht_List=[]
    for i in range(100):
        if random.randint(0,1)==1:
            ht_List.append('H')
        else:
            ht_List.append('T')

    counter=0
    previousflip=ht_List[0]
    for i in range(1,100):
        if ht_List[i]==previousflip:
            counter+=1
        else:
            counter=0
            previousflip=ht_List[i]
        if counter==6:
            numberOfStreaks+=1
            counter=0
print('streak: %s%%' % (numberOfStreaks / 100))
