import Mentifxxr

pin = input("Input Pin\n> ")
y = Mentifxxr.getInfo(pin)
word = input("What to say\n> ").replace(" ","_")

q = Mentifxxr.getActiveQuestion(y)
t = Mentifxxr.getType(y)

newid = Mentifxxr.getNewID()
Mentifxxr.awnser(q, t, newid, word)