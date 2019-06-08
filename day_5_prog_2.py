import random


announcedNumbers = []

def randNumGen(start,end):
	while(len(announcedNumbers) <= 89):
		num = random.randint(start,end)
		if num not in announcedNumbers:
			#input("PRESS TO CONTINUE....")		
			#print ("ANNOUNCED NUMBER is \t %d"%(num))
			announcedNumbers.append(num)
			
begin = 1
stop = 90
randNumGen(begin,stop)
announcedNumbers.sort()
#print(announcedNumbers)
#print(len(announcedNumbers))
empty=[]
for i in range(1,10):
    empty1=[]
    empty.append(empty1)

#print(empty)
m=0
for k in range (0,len(announcedNumbers)):
    empty[m].append(announcedNumbers[k])
    if(len(empty[m])==10):
        m=m+1
print(empty)
