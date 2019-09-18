import csv


data = {}

def extractData(file):
    

    with open(file,"r") as csv_file:
    	csv_dict_reader = csv.DictReader(csv_file)
    	for row in csv_dict_reader:
    	    data.update({len(data)+1:row})


def createDynamicDict(data,values_to_be_ignored):
    global featureDict
    print (data[1].keys(),values_to_be_ignored)
    featureDict={}
    features = data[1].keys()
    for value in values_to_be_ignored:
    	features.remove(value)

    for feature in features:
    	tempDict = {}
    	featureDict.update({feature:[]})
    	for datapoint in data.values():
    	    featureDict[feature].append(datapoint[feature])
    	featureDict[feature] = set(featureDict[feature])
    	for subfeature in featureDict[feature]:
	    tempDict.update({subfeature:[]})
	    featureDict[feature] = tempDict
def sortData():
    global featureDict
	
    for feature in featureDict:
	print (feature)
	for subfeature in featureDict[feature]:
	    for datapoint in data.values():
		if datapoint[feature] == subfeature:
		    featureDict[feature][subfeature].append(datapoint)

    print (featureDict)




	# file  = input("ENTER THE FILE NAME - ")
	file = "songData.csv"
	extractData(file)
	values_to_be_ignored = ["Song"]
	 # input("ENTER THE VALUES TO BE INGNORED AS COMMA SEPERATED VALUES - ").split(",")
	createDynamicDict(data,values_to_be_ignored)

	sortData()
