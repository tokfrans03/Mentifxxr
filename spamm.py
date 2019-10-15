import Mentifxxr
from threading import Thread


pin = 834333
y = Mentifxxr.getInfo(pin)
Mentifxxr.printInfo(y)

t = Mentifxxr.getActiveQuestionType(y)
q = Mentifxxr.getActiveQuestionid(y)

word = input("select word:\n> ")
i = int(input("times\n> "))

ids = []

idtred = []

def newid():
    global ids
    ids.append(Mentifxxr.getNewID())

for x in range(i):
    t1 = Thread(target = newid)
    idtred.append(t1)

for x in range(i):
    idtred[x].start()
    x += 1
    print(" Charging up:",  x, "/", i, end="\r")
print()
for x in range(i):
    idtred[x].join()
    x += 1
    print(" Waiting:",  x, "/", i, end="\r")

#print(len(idtred), ids)
x = 0

def send(q, t, z, y, word):
    Mentifxxr.awnser(q, t, z, y, word)

tred = []
for z in ids:
    x += 1
    t2 = Thread(target = send, args=(q, t, z, y, word,))
    tred.append(t2)
    print(" Packaging:", x , "/", i, end="\r")

print()
x = 0
input("\rPress enter to send")
for x in range(i):
    tred[x].start()
    x += 1
    print(" Sending:", x , "/", i, end="\r")