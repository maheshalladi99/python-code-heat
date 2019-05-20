def addition(b=[]):
    c=0
    for i in range(0,len(b)):
        c=c+b[i]
    print("addition",c)
    pass
d=[1,2,3,4]
addition(d)
def multiplication(b=[]):
    if(len(b)>0):
        c=1
        for i in range(0,len(b)):
            c=c*b[i]
        print("multiplication",c)
    else:
        print("no elements")
    pass
d=[1,2,3,4]

'''u=[]
z=int(input("enter the number of elements"))
for i in range(0,z):
    u.append(int(input()))
print(u)
multiplication(u)
'''
