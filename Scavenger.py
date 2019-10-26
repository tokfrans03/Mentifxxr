import Mentifxxr
from threading import Thread
from time import sleep

okpins = []
threads = []

begin = 880000
end = 881000

def getcode(pin):
    y = Mentifxxr.getInfo(pin, err=False)
    if (y == False):
        return
    x = Mentifxxr.listInfo(y)
    #print(x)
    global okpins
    okpins.append(x)
    #print(okpins)

for x in range(begin, end):
    t1 = Thread(target = getcode, args=(x,))
    threads.append(t1)
    #print(x)
    print("Loading: ", str(int(round((begin-x)/(begin-end), 2)* 100)) + "%", end="\r")

input("\nPress enter to begin getting codes")

for x in range(len(threads)):
    threads[x].start()
    print("Sending: ", str(int(round(x/(end-begin), 2)* 100)) + "%", end="\r")

print()

for x in range(len(threads)):
    threads[x].join()
    print("Waiting for response: ", str(int(round(x/(end-begin), 2)* 100)) + "%", end="\r")

print()

for x in okpins:
    print("\n" + "-" * 30 + "\n")
    for y in x:
        print(y)
print()
print("Result:\n")
print("Searched  " + str(end-begin) + " codes and", len(okpins), "was valid.", str(int(round(len(okpins)/(end-begin), 2) * 100)) + "%")