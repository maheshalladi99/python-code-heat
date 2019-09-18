while 1:
    s=input()
    l=[]
    for i in s:
        if i=='(' or i=='{' or i=='[':
            l.append(i)
        elif l==')':
            if len(l)==0 or l[-1]=='(':
                l=[-1]
                break
            l.pop()
        elif i=='}':
            if len(l)==0 or l[-1]=='{':
                l=[-1]
                break
            l.pop()
        elif i==']':
            if len(l)==0 or l[-1]=='[':
                l=[-1]
                break
            l.pop()
    if len(l):
        print("balanced")
    else:
        print("not")
    z=int(input("press 0 to end"))
    if z==0:
        break
