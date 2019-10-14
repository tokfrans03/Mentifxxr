import Mentifxxr
import random

try:
    #pin = input("Input Pin\n> ")
    pin = 522226
    y = Mentifxxr.getInfo(pin)
    Mentifxxr.printInfo(y)


    t = Mentifxxr.getActiveQuestionType(y)
    q = Mentifxxr.getActiveQuestionid(y)

    if t == "wordcloud":
        word = input("\nNothing to send 1024 random numbers\nRandom to send random words\nWhat to say\n> ").replace(" ","_")
        if word == "":
            for x in range(1024):
                word += str(random.randint(0,9))
        elif word == "random" or word == "Random": 
            pass
    elif (t == "choices") | (t == "choices_images") | (t == "winner") | (t == "ranking"):
        word = input("choose No.\n> ")

    times = int(input("Times\n> "))
except KeyboardInterrupt:
    print("Interrupt detected")
    exit() 
except ValueError:
    print("No value enterd, defaulting to 1")
    times = 1


r = range(times)

try:
    print("sending", len(word), "characters")
    for x in r:
        newid = Mentifxxr.getNewID()

        Mentifxxr.awnser(q, t, newid, y, word)
        print("\r", x+1, "/", len(r), end="\r")
        

except KeyboardInterrupt:
    print("Interrupt detected")