import random
import time

names = ("Jean_Luc", "Patrick Bateman", "Elidia ","Rob T", "Tyler Scotch", "Benjamin Bauer", "Satoshi Nakamoto")
facts = ("Boxing", "Mergers and Acquisitions ", "Biomedical", None, None, None, None, None, None, None, None, None, None)
points = 0


hobbiesData = ("basketball", "returninng Video Tapes", "football", " poetry", "drama", "history")


rand1 = random.randint(1,hobbiesData.__len__())

for i in range(len(names)):
    if(facts[i] == None):
        rand1 = random.randint(1, hobbiesData.__len__())

        if (hobbiesData[rand1] == None):
            #free give-away points
            facts[i] = names[i]
        else:
            print(facts[i])
            facts[i] = hobbiesData[rand1]
        hobbiesData[rand1] = None

    print(names[i], "associated with", facts[i])
    time.sleep(3)

for x in range(20):
    print(".")




