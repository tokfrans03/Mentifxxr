import Mentifxxr
import requests

pin = input("Input Pin\n> ")
# pin = "342239"
y = Mentifxxr.getInfo(pin)
Mentifxxr.printInfo(y)

t = Mentifxxr.getActiveQuestionType(y)
q = Mentifxxr.getActiveQuestionid(y)

i = y["id"]

newid = Mentifxxr.getNewID()

headers = {
    "x-identifier": newid,
    "cookie": "identifier1=" + newid,
    "Content-Type": "application/json",
}

a = requests.post(
    url="https://www.menti.com/core/quiz/" + i + "/players/" + newid, headers=headers
).text
print(a)
