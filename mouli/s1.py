##import pymongo
##
##myclient = pymongo.MongoClient("mongodb://localhost:27017/")
##mydb = myclient["mydatabase"]
##
##mycol = mydb["customers"]
##print(mydb.list_collection_names())
#student_count=(int(input("enter number of students: ")))
l1=[]
i=1
#for i in range(1,student_count+1):
##while True:
##    l2=[]
##    print("plz enter",i," student name: ")
##    f_1=input()
##    l2.append(f_1)
##    print("plz enter",i," student roll number: ")
##    f_2=input()
##    l2.append(f_2)
##    print("plz enter",i," student branch: ")
##    f_3=input()
##    l2.append(f_3)
##    l1.append(l2)
##    i+=1
##print(l1)
l1=[['mahesh', '1', 'ece'], ['hasini', '2', 'cse'], ['rajesh', '3', 'ece'], ['venkat', '4', 'civil'], ['kishore', '5', 'cse'], ['surya', '6', 'mech'], ['subhash', '4', 'cse'], ['jeddi', '8', 'eee'], ['vimal', '1', 'eee']]
l3=[]
for i in range(0,len(l1)):
    if ece in l1[i]:
        print(l1[i])
        l3.append(l1[i])



