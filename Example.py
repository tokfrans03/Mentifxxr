import Mentifxxr
import random

try:
    pin = input("Input Pin\n> ")

    while 1:
        print()
        try: 

            y = Mentifxxr.getInfo(pin)
            Mentifxxr.printInfo(y)

            wordlist = ["favor", "heavyweight", "became", "habit", "battleground", "growl", "fundamental", "rear", "estimate", "quantum", "soon", "ambitious", "grappler", "limitless", "nuclear", "bluster", "teeth", "crutch", "pigeon", "bed"]

            t = Mentifxxr.getActiveQuestionType(y)
            q = Mentifxxr.getActiveQuestionid(y)

            if (t == "wordcloud"):
                word = input("\nNothing to send 1024 random numbers\nRandom to send random words\nWhat to say\n> ").replace(" ","_")
                if word == "":
                    for x in range(1024):
                        word += str(random.randint(0,9))
                elif word == "random" or word == "Random": 
                    word = wordlist
            elif (t == "choices") | (t == "choices_images") | (t == "winner") | (t == "ranking"):
                word = int(input("choose No.\n> "))
            elif (t == "open"):
                while 1:
                    word = input("Nothing to enter 250 random numbers\nMust be less than 250 chars\n> ")
                    if word == "":
                        for x in range(250):
                            word += str(random.randint(0,9))
                        break
                    elif len(word) < 250:
                        break
            elif t == "scales":
                word1 = []
                word = {}
                print("Enter a value for each question with a value from", str(Mentifxxr.getActiveQuestionMinMax(y)["min"]) + "-" + str(Mentifxxr.getActiveQuestionMinMax(y)["max"]), "or nothing to skip")
                while len(word1) < len(Mentifxxr.getActiveQuestion(y)):
                    try:
                        e = input("> ")
                        if e == "":
                            pass
                        else:
                            e = int(e)
                            if (e <= Mentifxxr.getActiveQuestionMinMax(y)["max"]) & (e >= Mentifxxr.getActiveQuestionMinMax(y)["min"]):
                                word1.append(e)
                            else:
                                print("Value too small or large, try again")
                    except ValueError:
                        pass
                    if e == "":
                        word1.append(e)

                print(Mentifxxr.getActiveQuestion(y)) 
                for z in Mentifxxr.getActiveQuestion(y):
                    for x in range(1, len(word1) + 1):
                        if word1[x - 1] == "":
                            word[z["id"]] = "other"
                        else:
                            word[z["id"]] = [word1[x - 1], 1]
                print(word)
            elif t == "qfa":
                word = input("Your question\n> ")

            times = int(input("Times\n> "))

        except KeyboardInterrupt:
            print("Interrupt detected")
            exit() 
        except ValueError:
            times = 1
            print("No value enterd, defaulting to 1")


        r = range(times)
        

        if word == "wordlist":
            r = wordlist

        try:
            print("sending", len(word), "characters")
            for x in r:
                newid = Mentifxxr.getNewID()
                if word == "wordlist":
                    Mentifxxr.awnser(q, t, newid, y, x)
                    
                else:
                    Mentifxxr.awnser(q, t, newid, y, word)
                    print("\r", x+1, "/", len(r), end="\r")
        except KeyboardInterrupt:
            print("Interrupt detected, Quitting")
            exit()
            

except KeyboardInterrupt:
    print("Interrupt detected, Quitting")