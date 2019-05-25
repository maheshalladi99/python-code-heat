import csv
data={}
def extractData(file):
    with open(file,"r") as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)
        for row in csv_dict_reader:
            data.update({len(data)+1:row})
        print(data)    
def createDynamicDict(data,value_to_be_ignored):
    global featureDict
    print(data[1].keys(),value_to_be_ignored)
    futureDict={}
    features=data[1].keys()
    for value in value_to_be_ignored:
        tempDict={}
        featureDict.update({feature:[]})
        for datapoint in data.values():
            featureDict[feature].append(datapoint[feature])
	featureDict[feature] = set(featureDict[feature])

	for subfeature in featureDict[feature]:
	    tempDict.update({subfeature:[]})
	featureDict[feature] = tempDict
    #print(featureDict)

def sortData():
    global featureDict
    for feature in featureDict:
        print (feature)
        for subfeature in featureDict[feature]:
           for datapoint in data.values():
               if datapoint[feature]==subfeature:
                   featureDict[feature][subfeature].append(datpoint)
    print(featureDict)
    
    
file=("SongData3.csv")

extractData(file)
value_to_be_ignored = ["song"]
createDynamicDict(data,value_to_be_ignored)
sortData()
