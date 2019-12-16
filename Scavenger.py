import Mentifxxr
from threading import Thread
from time import sleep
from collections import Counter
from collections import OrderedDict
from etaprogress.progress import ProgressBar

okpins = []
data = []
threads = []
maxthreads = 5
err = 0
wait = 0

showresults = False

begin = 800000
end = 801000

bar = ProgressBar(end-begin, max_width=100)

def getcode(pin):
    y = Mentifxxr.getInfo(pin, err=False)
    if (y == False):
        return
    try:
        x = Mentifxxr.listInfo(y)
    except:
        return False
    activeid = y["pace"]["active"]
    #print(x)
    global okpins
    okpins.append(x)
    for z in y["questions"]:
        if z["id"] == activeid:
            data.append(z["type"])
    #print(okpins)



for x in range(begin, end):
    t1 = Thread(target = getcode, args=(x,))
    threads.append(t1)
    #print(x)
    
    print("Loading: ", str(round( (((x-begin)/(end-begin)) * 100), 1)) + "%", end="\r")

input("\nPress enter to begin getting codes")

for x in range(len(threads)):
    try:
        threads[x].start()
        threads[x-maxthreads].join()
        sleep(wait)
    except:
        err += 1
    bar.numerator = x
    print(bar, end="\r")
    #print("Sending: ", str(round(float((x/(end-begin))* 100), 4)) + "%     ", end="\r")

print()


print()
print("Result:\n")
print("Searched  " + str(end-begin) + " codes and", len(okpins), "was valid with", err, "errors.", str(int(round(len(okpins)/(end-begin), 2) * 100)) + "%")

print("Statistics:")
print("-" * 30 + "\n")

l = Counter(data)
l = OrderedDict(sorted(l.items(), key=lambda t: t[1], reverse=True))

for x, y in l.items():
    print(x + ":", y)

#if input("Do you want to see all the results? (1/0 True/False)") == True:

for x in okpins:
    print("\n" + "-" * 30 + "\n")
    for y in x:
        print(y)