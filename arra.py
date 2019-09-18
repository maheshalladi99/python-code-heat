a=[1,1,2,3,3,4,2,5,5,6]
count=0
j=0
for i in range(0+j,len(a)):
    count=0
    for j in range(i,len(a)):
        if(a[i]==a[j]):
            count=count+1
        if(a[i]!=a[j]):
            break
    print("(",a[i],",",count,")")
        
    
