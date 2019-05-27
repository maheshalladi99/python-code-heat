l=['a','b','c','d']
'''if 'e' in l:
    print("exists")
else:
    l.append('e')
print(l)'''
a=1
for i in range(0,len(l)):
    if('e'==l[i]):
        print("exists")
    elif('e'!=l[i]):
        l.append('e')
print(l)        
