e1=[]
e2=[]
o=[]
l=[]
dup1=[]
dup2=[]
m=0
o!=e1
for i in range(1,101):
    l.append(int(i))
for i in range(0,10):
    em=[]
    e1.append(em)
    #o.append(em)
#print(e)
#print(len(e))
#print(o)
for j in range(0,100):
    if(l[j]%2==0):
        dup1.append(l[j])
        #print(l[j],end=" ")
#print("\n",len(dup1))
for k in range (0,50):
    e1[m].append(dup1[k])
    if(len(e1[m])==5):
        m=m+1
print(e1)
#print(o)
#print(l)

m=0
#for i in range(1,101):
    #l.append(int(i))
for i in range(0,10):
    em=[]
    e2.append(em)
    #o.append(em)
#print(e)
#print(len(e))
#print(o)
for j in range(0,100):
    if(l[j]%2!=0):
        dup2.append(l[j])
        #print(l[j],end=" ")
#print("\n",len(dup1))
for k in range (0,50):
    e2[m].append(dup2[k])
    if(len(e2[m])==5):
        m=m+1
print(e2)
