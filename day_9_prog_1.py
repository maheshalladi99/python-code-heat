#file handling
import csv
csvfile="SongData.csv"
with open(csvfile,"w",newline="\n") as csv_file:
    csv_writer=csv.writer(csv_file)
    li=["s.no","song","lyricist","md","genre"]
    csv_writer.writerow(["s.no","song","lyricist","md","genre"])
    #for i in range(1,len(li)):
        #csv_writer.writerow([i,str(input("enter song name: ")),str(input("enter lyricist name: ")),str(input("enter music director name: ")),str(input("enter genre name: "))])
    csv_writer.writerow(["1","s1","l1","m1","g1"])
    csv_writer.writerow(["2","s2","l2","m2","g2"])
    csv_writer.writerow(["3","s3","l2","m2","g2"])
    csv_writer.writerow(["4","s4","l3","m2","g3"])
    csv_writer.writerow(["5","s5","l4","m2","g1"])
    csv_writer.writerow(["6","s6","l2","m2","g2"])
csvfile_1="SongData2.csv"
with open(csvfile_1,"w",newline="\n") as csv_file:
    features=["song","lyricist","md","genre"]
    csv_dict_writer=csv.DictWriter(csv_file,fieldnames=features)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerow({"song":"s1","lyricist":"l1","md":"m1","genre":"g1"})
    csv_dict_writer.writerow({"song":"s2","lyricist":"l2","md":"m2","genre":"g2"})
    csv_dict_writer.writerow({"song":"s3","lyricist":"l3","md":"m3","genre":"g3"})
    csv_dict_writer.writerow({"song":"s4","lyricist":"l2","md":"m4","genre":"g1"})
    csv_dict_writer.writerow({"song":"s5","lyricist":"l4","md":"m2","genre":"g4"})
    csv_dict_writer.writerow({"song":"s6","lyricist":"l2","md":"m4","genre":"g2"})
'''
with open(csvfile,"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
        
	
with open(csvfile_1,"r") as csv_file:    
    csv_dict_reader = csv.DictReader(csv_file)
    for row in csv_dict_reader:
        print(row)
	'''
