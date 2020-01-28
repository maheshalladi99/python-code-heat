def main():
    s=input("Enter the string :").split(" ")
    def position():
        try:
            n=int(input("Enter the position :"))
            if(n>len(s)+1):
                print("invalid position,please enter once again")
                position()
            else:
                t=input("Enter the required word or string :")
                s.insert(n-1,t)
                k=' '
                k=k.join(s)
                print("The string after insertion is :",end="")
                print(k)
        except:
            print("invalid format")
            position()
    position()
main()
