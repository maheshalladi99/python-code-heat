l=[]
n1=[]
n2=[]
n3=[]
n4=[]
n5=[]
n6=[]
n7=[]
n8=[]
n9=[]
n10=[]
k=[]
p=[]
o1=[]
o2=[]
q=[]

for i in range(1,101):
    l.append(i)
#print(l)
#print("even no. are")
for j in range(0,100):
    if(l[j]%2==0):
        if(l[j]<=10):
            n1.append(l[j])
        elif(l[j]>10 and l[j]<=20):
            n2.append(l[j])
        elif(l[j]>20 and l[j]<=30):
            n3.append(l[j])
        elif(l[j]>30 and l[j]<=40):
            n4.append(l[j])
        elif(l[j]>40 and l[j]<=50):
            n5.append(l[j])
        elif(l[j]>50 and l[j]<=60):
            n6.append(l[j])
        elif(l[j]>60 and l[j]<=70):
            n7.append(l[j])
        elif(l[j]>70 and l[j]<=80):
            n8.append(l[j])
        elif(l[j]>80 and l[j]<=90):
            n9.append(l[j])
        elif(l[j]>90 and l[j]<=100):
            n10.append(l[j])
        #print(l[j],end=" ")
print("\n")
p.append(n1)
p.append(n2)
p.append(n3)
p.append(n4)
p.append(n5)
p.append(n6)
p.append(n7)
p.append(n8)
p.append(n9)
p.append(n10)
print("seperated lists are :")
print(p)
print("\nodd no. are")
for j in range(0,100):
    if(l[j]%2 != 0):
       if(l[j]<=10):
            n1.append(l[j])
        elif(l[j]>10 and l[j]<=20):
            n2.append(l[j])
        elif(l[j]>20 and l[j]<=30):
            n3.append(l[j])
        elif(l[j]>30 and l[j]<=40):
            n4.append(l[j])
        elif(l[j]>40 and l[j]<=50):
            n5.append(l[j])
        elif(l[j]>50 and l[j]<=60):
            n6.append(l[j])
        elif(l[j]>60 and l[j]<=70):
            n7.append(l[j])
        elif(l[j]>70 and l[j]<=80):
            n8.append(l[j])
        elif(l[j]>80 and l[j]<=90):
            n9.append(l[j])
        elif(l[j]>90 and l[j]<=100):
            n10.append(l[j])
        print(l[j],end=" ")
q.append(o1)
q.append(o2)
print("\n ",q)
    

    
