import Mentifxxr
import random

try:
    pin = input("Input Pin\n> ")
    y = Mentifxxr.getInfo(pin)
    Mentifxxr.printInfo(y)


    word = input("What to say\nNothing to send 1024 random numbers\nRandom to send random words\n> ").replace(" ","_")

    if word == "":
        for x in range(1024):
            word += str(random.randint(1,9))
    elif word == "random" or word == "Random":
        pass

    times = int(input("Times\n> "))
except KeyboardInterrupt:
    print("Interrupt detected")
    exit() 

t = Mentifxxr.getType(y)
q = Mentifxxr.getActiveQuestion(y)

r = range(times)

try:
    print("sending", len(word))
    for x in r:
        newid = Mentifxxr.getNewID()

        Mentifxxr.awnser(q, t, newid, word)
        print("\r", x+1, "/", len(r), end="\r")
        

except KeyboardInterrupt:
    print("Interrupt detected")