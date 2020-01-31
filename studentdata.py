'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
a=int(input("enter student count:"))
l=[]
for i in range(0,a):
    l1=[]
    l.append(l1)
#print(l)
for i in range(0,a):
    print("enter ",i+1,"student name:",end="")
    n=input()
    l[i].append(n)
    print("enter ",i+1,"Roll number:",end="")
    r=input()
    l[i].append(r)
    print("enter ",i+1,"City:",end="")
    c=input()
    l[i].append(c)
    print("enter ",i+1,"Mobile number:",end="")
    m=input()
    l[i].append(m)
dum=[]
for p in range(0,a):
    for q in range(0,len(l[p])):
        dum.append(l[p][q])
print(l)
##################################################
while(True):
    def details(givendata):
        if givendata not in dum:
            print("Details not found")
        for i in range(0,a):
            if givendata in l[i]:
                print("results found")
                print("Name of sudent:",l[i][0])
                print("roll of sudent:",l[i][1])
                print("city of sudent:",l[i][2])
                print("Mobile Number of sudent:",l[i][3])   
  
        #else:
            #print("Details not found")
    print("you options are \n1.Name \n2.Roll number \n3.City \n4.Mobile number")
    option=int(input("your option is:"))
    if option==1:
        name=input("Enter name:")
        details(name)
    if option==2:
        name=input("Enter roll no.:")
        details(name)
    if option==3:
        name=input("Enter City:")
        details(name)
    if option==4:
        name=input("Enter mobile:")
        details(name)
    #roll=input("enter roll number:")
    
    q=input("you want exit then press x")
    if(q=="x"):
        break
