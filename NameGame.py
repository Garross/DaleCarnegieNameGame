import random
import time

names = ["Jean_Luc", "Patrick Bateman", "Elidia ","Rob T", "Tyler Scotch", "Benjamin Bauer", "Satoshi Nakamoto"]
facts = ["Boxing", "Mergers and Acquisitions", "Biomedical", None, None, None, None]
points = 0


hobbiesData = ["basketball", "returninng Video Tapes", "football", "poetry", "drama", "history"]


for i in range(len(names)):
    if(facts[i] == None):
        
        rand1 = random.randint(0, hobbiesData.__len__()-1)
        while(hobbiesData[rand1] == None):
            rand1 = random.randint(0, hobbiesData.__len__()-1)
        
        facts[i] = hobbiesData[rand1]
        hobbiesData[rand1] = None

    print(names[i], "associated with", facts[i])
    time.sleep(2)
    
time.sleep(5)

for x in range(200):
    print(".")

x = [0,1,2,3,4,5,6]

for i in range(len(facts)):
    
    rand1 = random.randint(0, x.__len__()-1)
    while(x[rand1] == None):
        rand1 = random.randint(0, hobbiesData.__len__()-1)
    
    x[rand1] = None
    
    print("Who is associated with ",facts[rand1],"?",  sep='')
    
    inp = input("Enter the name: ") 
    
    if(str.upper(inp) == str.upper(names[rand1])):
        points = points + 1
        print("correct")
    else:
        print("kys", " it was ", names[rand1], sep = "")
        
print("you only got ", points, " points, haha")