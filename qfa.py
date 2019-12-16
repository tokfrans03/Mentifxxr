import Mentifxxr
import requests

pin = input("Input Pin\n> ")
# pin = "342239"
y = Mentifxxr.getInfo(pin)
Mentifxxr.printInfo(y)

t = Mentifxxr.getActiveQuestionType(y)
q = Mentifxxr.getActiveQuestionid(y)

# print(t, q)
word = input("select word:\n> ")


newid = Mentifxxr.getNewID()

Mentifxxr.awnser(q, t, newid, y, word)

