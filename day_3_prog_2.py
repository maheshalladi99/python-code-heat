text = ["NAME","NO:","CITY"]
users = []
n=int(input("ENTER THE NO OF USERS : "))
for i in range(1,n+1):
    l = []
    print("USER DATA ",i)
    for j in range(0,3):
        print(text[j],end=" ")
        l.append(input(": "))
    users.append(l)
#print("THE COMPLETE DATA OF USERS IS: ")
#print(users)
print("enter user data number:")
l=int(input())
print(users[l-1])
    
