#task
e1=[]
n=int(input("enter the users count: "))
for i in range(0,2):
    em=[]
    e1.append(em)
for i in range (1,n+1):
    print(i,"st",end=" ")
    name=input("USER NAME: ")    
    e1[0].append(name)
    print(i,"st",end=" ")
    pswd=input(" PASSWPRD: ")
    e1[1].append(pswd)
print(e1)
print("NO OF USER YOUR HAVING IS ",len(e1[0]))
while(True):
    s=int(input("GIVE THE REQUIRED USER NUMBER INFORMATION: "))
    print("USER NAME ",s,"IS: ")
    print(e1[0][s-1])
    print("PASWORD OF",s,"IS:")
    print(e1[1][s-1])
