e=[]
o=[]
l=[]
dup1=[]
l=0
for m in range(1,101):
    l[m]=m
for i in range(0,10):
    em=[]
    e.append(em)
    o.append(em)
print(e)
print(o)

for j in range(0,100):
    if(l[j]%2==0):
        dup1.append(l[j])
        #print(l[j],end=" ")
print("\n",len(dup1))
#for l in range (0,10):
for k in range (0,49):
    e[l].append(dup1[k])
    if(len(e[l]==5)):
        l=l+1
    
print(e)
