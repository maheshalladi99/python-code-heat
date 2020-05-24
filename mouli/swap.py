while(True):
    
    f=int(input())
    d=input()
    a=list(d)
    number=int(d)
    c=len(a)
    swap_number=a
    count=0
    for i in range(0,f):
        for j in range(0,c-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                str1=""
                x=str1.join(a)
                swap_number=int(x)            
                if(swap_number < number):
                    #print((swap_number))
                    count=count+1
                    a=list(str((swap_number)))
                    if(count == f):
                        print(swap_number)
                    break        
        else:
            print(d)
    
