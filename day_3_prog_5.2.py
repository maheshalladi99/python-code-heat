e1=[]
o=[]
l=[]
dup1=[]
dup2=[]
m=0
o!=e1
for i in range(1,1001):
    l.append(int(i))
for i in range(0,100):
    em=[]
    e1.append(em)
    #o.append(em)
#print(e)
#print(len(e))
#print(o)
for j in range(0,1000):
    if(l[j]%2==0):
        dup1.append(l[j])
        #print(l[j],end=" ")
#print("\n",len(dup1))
for k in range (0,499):
    e1[m].append(dup1[k])
    if(len(e1[m])==5):
        m=m+1
print(e1)
#print(o)
#print(l)
for i in range(0,100):
    em=[]
    #e1.append(em)
    o.append(em)
#print(e)
#print(len(e))
#print(o)
for j in range(0,1000):
    if(l[j]%2!=0):
        dup2.append(l[j])
        #print(l[j],end=" ")
#print("\n",len(dup1))
#print(dup2)
#print(o)
m=0
for k in range (0,len(dup2)):
    o[m].append(dup2[k])
    if(len(o[m])==5):
        m=m+1
print(o)
