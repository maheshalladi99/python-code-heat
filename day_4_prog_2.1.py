#atm task part2
e1=[]
n=int(input("enter the users count: "))
for i in range(0,3):
    em=[]
    e1.append(em)
for i in range (1,n+1):
    print(i,end=" ")
    name=input("USER NAME: ")    
    e1[0].append(name)
    print(i,end=" ")
    mb_no=input("MOBILE NUMBER: ")
    e1[1].append(mb_no)
    print(i,end=" ")
    add=input("ADDRESS: ")
    e1[2].append(add)
#print(e1)
#print("sucessfully registered")
    
