import random

from  tkinter import *



def numberGen():
	global tic

	usedNumbers = []

	start = 1

	r1 = 1
	r2 = 10
	ticket = []
	for i in range(r1,r2):
		# print "START",start
		n1 = random.randint(start,start+9)
		n2 = random.randint(start,start+9)
		while n1==n2:
			n1 = random.randint(start,start+9)
			n2 = random.randint(start,start+9)	

		start+=10
		# print n1,n2
		ticket.append(n1)
		ticket.append(n2)

	print(ticket)

	tic = random.sample(ticket,15)
	tic.sort()
	print(tic)

def strikedown():
	global e 
	string = e.get()
	print(string)
	v = Label(numberFrame, width = 10,text=string,fg = "red")
	print (valDict[string],"NUMBER")
	if (len(string) == 1):

		v.grid(row=int(valDict[string]), column=0)
	else:
		v.grid(row=int(valDict[string]), column=int(string[0]))
	
 

window = Tk()
window.title('HousieTicket')

# titleFrame = Frame(window)
# titleFrame.pack(side=)
# Label(titleFrame, text="HOUSIE TICKET")



numberFrame = Frame(window)
numberFrame.pack()

buttonFrame = Frame(window)
buttonFrame.pack(side=BOTTOM)



Label(buttonFrame, text="Number here:").grid(row=20, column=3,columnspan=2, rowspan=2,sticky=W)
e = Entry(buttonFrame)
e.grid(row=22, column=3)
print (e,"asdf")
Label(buttonFrame, text="Strike").grid(row=24, column=3,columnspan=2, rowspan=2,sticky=W)
Button(buttonFrame, width = 20,command=strikedown).grid(row=26, column=3)






row=0
col=0
k=0

valDict = {}

skip = random.sample([0,1,2],2)
colCount = 0
numberGen()

for value in tic:
	if (colCount < 2):
		v = 'e_'+str(value) 
		v = Label(numberFrame, width = 10,text=str(value),fg = "green")
		if (len(str(value)) == 1):
			v.grid(row=skip[colCount], column=0,columnspan=1, rowspan=1,
               sticky=W+E+N+S, padx=5, pady=5)
		else:
			v.grid(row=skip[colCount], column=int(str(value)[0]),columnspan=1, rowspan=1,
               sticky=W+E+N+S, padx=5, pady=5)
		valDict.update({str(value):skip[colCount]})

		if(value == 60):
			print (value,colCount,skip[colCount])
		colCount+=1

	if (colCount == 2):
		colCount = 0
		skip = random.sample([0,1,2],2)

	
print(valDict)

# 
window.mainloop()
