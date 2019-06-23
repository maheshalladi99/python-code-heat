#atm task full(completed)(fix it for all executions)
e1=[]
print("enter the user count :")
n=int(input(""ENTER THE USER COUNT"enter the users count: "))
for i in range(0,6):
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
print("sucessfully registered")
a=99665916
b=1008
for i in range(1,n+1):    
    print(i,"user ACCOUNT NUMBER IS: ",a)
    print(i,"user ACCOUNT PASSWORD IS: ",b)
    m=int(input("Please deposit money: "))
    e1[3].append(a)
    e1[4].append(b)
    e1[5].append(m)
    a+=1
    b+=1
#print(e1)
############################################################################
def amountfun(amount):
    if (amount <= e1[5][pd1]):
        
        
        print("take the amount: ",amount)
        print("your balance is: ",e1[5][pd1]-amount) 
    
while(1):
    print("LOGIN PLEASE: ")
    a1=int(input("ENTER THE ACCOUNT NUMBER: "))
    if(a1 in e1[3]):
        p1=int(input("ENTER THE password: "))
        #pd2 = e1[4].index(p1)
        pd1 = e1[3].index(a1)
            
        if(p1 == e1[4][pd1]):
            print("ENTER THE CHOISE BELOW")
            print("1. Withdrawal      2. Deposit")
            inp=int(input("ENETR THE CHOOSEN OPTION HERE: "))
            
            if(inp == 1):
                amoun=int(input("Enter the amount: "))
                if (amoun <= e1[5][pd1]):                   
                           print("take the amount: ",amoun)
                           print("your balance is: ",e1[5][pd1]-amoun)                    
                else:
                            
                           print("ivalid amount")
                           amountfun(amoun)
                           
                           
            if(inp == 2):
                           amount=int(input("Enter  the amount: "))
                           print("your balance is: ",e1[5][pd1]+amount)                                      
        else:               
            print("invalid password")
    else:
        print("invlid account number")
