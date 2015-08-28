import json, sys

cardList = {
	"cards": [
	{
		"title": "atlantis",
		"date": "5/5/2005",
		"eval": 122,
		"result": "success",
		"completed": True
	},
	{
		"title": "hotdog",
		"date": "5/7/2005",
		"eval": 412,
		"result": "participated",
		"completed": True
	},
	{
		"title": "atlantis",
		"date": "5/6/2005",
		"eval": 162,
		"result": "failure",
		"completed": False
	}],

};

bgCards = {
    "cards": [
    {
    	"title":"Lanterns",
    	"nump":2,
    	"date":"8/15/2015",
    	"result":"win"
    },
    {
    	"title":"Indigo",
    	"nump":2,
    	"date":"8/15/2015",
    	"result":"win"
    },
    {
    	"title":"Indigo",
    	"nump":2,
    	"date":"8/15/2015",
    	"result":"win"
    },
    {
    	"title":"Formula D",
    	"nump":10,
    	"date":"8/15/2015",
    	"result":"loss"
    },
    {
    	"title":"Sheriff of Nottingham",
    	"nump":4,
    	"date":"8/20/2015",
    	"result":"loss"
    }]
};

configCards = {
    "eval" : "singleNumber",
    "date" : "frequency",
    "result" : "frequency",
    "completed" : "percentage",
    "title" : "frequency"
}

configBGCards = {
    "title":"frequency",
    "date": "frequency",
    "result": "frequency",
    "nump":"singleNumber"
}

def analyze(groupOn, cards, report, config):
    for card in cards:
        if "totalCards" in report:
            report["totalCards"] = int(report["totalCards"]) + 1
        else:
            report["totalCards"] = 1

        groupOnVal = card[groupOn]
		
        if groupOnVal in report:
            reportCard = report[groupOnVal]
        else:
            report[groupOnVal] = {}
            reportCard = report[groupOnVal]
            
        if "totalCards" in reportCard:
            reportCard["totalCards"] = int(reportCard["totalCards"]) + 1
        else:
            reportCard["totalCards"] = 1
		    
        for key, value in card.items():

            if key == groupOn:
                continue

            if key not in reportCard:
                reportCard[key] = createReportForKey(key, config)

            evalForKey(value, reportCard, key, config)
		 
		 
		 
			
    return report

def createReportForKey(key, config):
    dict = {}
    type = config[key]

    if type == "singleNumber":
        dict["highest"] = 0
        dict["lowest"] = sys.maxsize
        dict["count"] = 0
        dict["average"] = 0
        dict["frequency"] = {}

    return dict

def evalForKey(cardValue, report, key, config):
    if config[key] == "singleNumber":
        evalSingleNumber(cardValue, report[key])
    elif config[key] == "frequency":
        evalFrequency(cardValue, report[key])
        
def evalSingleNumber(cardValue, report):
    if cardValue > report["highest"]:
        report["highest"] = cardValue
        
    if cardValue < report["lowest"]:
        report["lowest"] = cardValue
        
    report["average"] = ((report["average"] * report["count"]) + cardValue) / (report["count"] + 1)

    report["count"] = report["count"] + 1
    
    if cardValue not in report["frequency"]:
        report["frequency"][cardValue] = 1
    else:
        report["frequency"][cardValue] = report["frequency"][cardValue] + 1

def evalFrequency(cardValue, report):
    if cardValue not in report:
        report[cardValue] = 1
    else:
        report[cardValue] = report[cardValue] + 1

def addToTree(root, array):
	currentNode = root
	
	for value in array:
		if value not in currentNode:
			currentNode[value] = {}
			currentNode[value]["_t"] = 1
		else:
			currentNode[value]["_t"] = currentNode[value]["_t"] + 1

		currentNode = currentNode[value]

report = {}
report = analyze("result", bgCards["cards"], report, configBGCards)
print(json.dumps(report, indent=3, sort_keys=True))

tree = {}
moves1 = ["20h1","5a3","14h7","17b3","4d7"]
moves2 = ["20h1","5a3","1h7","2b3","3e4"]
addToTree(tree, moves1)
addToTree(tree, moves2)
print(json.dumps(tree, indent=3, sort_keys=True))