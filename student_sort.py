# Student Data Structure
students = {}
def createDynamicDict():
	global sortDict
	sortDict = {}
	features = students[1].keys()
	for feature in features:
		sortDict.update({feature:[]})
		if feature != "Name":
			for value in students.values():
				sortDict[feature].append(value[feature])

	# print (sortDict)
	for feature,lst in zip(sortDict.keys(),sortDict.values()):
		sortDict.update({feature:set(lst)})
	# print (sortDict)

	for feature,value in zip(sortDict.keys(),sortDict.values()):
		d = {}	
		for element in value:
			d.update({element:[]})
		sortDict.update({feature:d})
	
	# print (sortDict)		


def sortByGender():
	global sortDict
	for gender in sortDict["Gender"].keys():
		for data in students.values():
			if data["Gender"] == gender:
				sortDict["Gender"][gender].append(data)
	print sortDict["Gender"]			 

def sortByBranch():
	global sortDict
	for branch in sortDict["Branch"].keys():
		for data in students.values():
			if data["Branch"] == branch:
				sortDict["Branch"][branch].append(data)
	print sortDict["Branch"]			 
 

def sortByCollege():
	global sortDict
	for college in sortDict["College"].keys():
		for data in students.values():
			if data["College"] == college:
				sortDict["College"][college].append(data)
	print sortDict["College"]			 


def addStudent():
	print "***** WELCOME TO STUDENT ENROLLING PROCESS ******\
	PLEASE PROVIDE THE FOLLOWING DATA TO ENROLL."

	name = raw_input("NAME - ")
	branch = raw_input("BRANCH - ")
	college = raw_input("COLLEGE - ")
	gender = raw_input("GENDER - ")

	if len(students) > 0:
		students.update({
			list(students.keys())[-1]+1:{
					"Name":name,
					"Branch":branch,
					"College":college,
					"Gender":gender
				}
			})
	else:
		# FIRST ENTRY IN THE DICTIONARY
		students.update({
			1:{
					"Name":name,
					"Branch":branch,
					"College":college,
					"Gender":gender
				}
			})
			
	print students
if __name__ == '__main__':

	# Execution starts from here.
	while True:
		choice = int(raw_input("1.Enroll 2.Sort"))
		if (choice == 1):
			addStudent()
		elif(choice == 2):
			if (len(students) == 1):
				print "NO STUDENT ENROLLED"
			else:
				createDynamicDict()
				choice = int(raw_input("Sorting By 1.Gender 2.Branch 3.College"))
				if (choice == 1):
					sortByGender()
					pass
				elif(choice == 2):
					sortByBranch()
					pass 
				elif(choice == 3):
					sortByCollege()
					pass
				else:
					print "INVALID"
				
		else:
			print "INVALID"
