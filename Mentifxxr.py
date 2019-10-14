import json
import requests


def getNewID():
    x = json.loads(requests.post('https://www.menti.com/core/identifier').text)
    return x["identifier"]

def getInfo(pin):
    x = requests.get('https://www.menti.com/core/objects/vote_ids/' + str(pin)).text
    try:
        (json.loads(x))["id"]
        return json.loads(x)
    except KeyError:
        print("ERR: No such code")
        exit()

def printInfo(info):
    activeid = info["pace"]["active"]
    print("Name:\t\t", info["name"])
    print("id:\t\t", info["id"])
    for x in info["questions"]:
        if x["id"] == activeid:
            print("Type:\t\t", x["type"])
            print("Question:\t", x["question"])
            print("Public Key:\t", x["public_key"])

def getActiveId(info):
    return info["pace"]["active"]

def getActiveQuestion(info):
    activeid = info["pace"]["active"]
    for x in info["questions"]:
        if x["id"] == activeid:
            return x["public_key"]

def getType(info):
    activeid = info["pace"]["active"]
    for x in info["questions"]:
        if x["id"] == activeid:
            return x["type"]

def awnser(Questionid, type, ID, awnser):
    #print(len(awnser), type)
    """    if ((len(awnser) > 25 ) & (type == "worldcloud")):
        print("ERR: can't be more that 25 characters")
        exit()"""

    data = {"question_type":type,"vote":awnser}

    headers = {
    "x-identifier":ID,
    "cookie": "identifier1=" + ID,
    "Content-Type":"application/json",
    }
    
    requests.post(url = 'https://www.menti.com/core/votes/' + Questionid, data = json.dumps(data), headers=headers)

"""
try:
    pin = 569245
    word = "small_Brain"

    pin = input("Input Pin\n> ")
    y = getInfo(pin)
    
    word = input("What to say\n> ").replace(" ","_")
    times = int(input("Times\n> "))
    
    printInfo(y)
    q = getActiveQuestion(y)
    for x in y["questions"]:
        if x["id"] == q:
            t = x["type"]
            print(x["type"])
    t = "wordcloud"

    r = range(times)

    for x in r:
        newid = getNewID()
        awnser(q, t, newid, word)
        print("\r", x+1, "/", len(r), end="\r")
        

except KeyboardInterrupt:
    print("Interrupt detected")

"""