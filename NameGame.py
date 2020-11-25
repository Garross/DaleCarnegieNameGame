import random
import time
#Quickly hacked together code...

#Example Arrays
names = ["Jean_Luc", "Patrick Bateman", "Elidia","Rob T", "Tyler Scotch", "Benjamin Bauer", "Satoshi Nakamoto"]
presetFacts = ["Boxing", "Mergers and Acquisitions", "Biomedical", None, None, None, None]
points = 0

#Example Hobbies and Facts about people to help you remember their names.
hobbiesAndFacts = ["basketball", "returninng Video Tapes", "football", "poetry", "drama", "history"]

#Printing all Name vs Hobby/Fact pairs for the user to memorize.
for i in range(len(names)):
    # Matching names to a hobby or fact about the person if there is no preset fact.
    if(presetFacts[i] == None):

        rand1 = random.randint(0, hobbiesAndFacts.__len__()-1)
        #Searches for a new random Hobby/Fact if the random one selected has already been used and is now equal
        #to none.
        while(hobbiesAndFacts[rand1] == None):
            rand1 = random.randint(0, hobbiesAndFacts.__len__()-1)
        
        presetFacts[i] = hobbiesAndFacts[rand1]
        hobbiesAndFacts[rand1] = None

    #Give the user time to memorize the names and facts.
    print(names[i], "associated with", presetFacts[i])
    time.sleep(2)
    
time.sleep(5)

#Move the answers out of sight by filling up the console.
for x in range(200):
    print(".")

#Asking the user to guess the names in random order.
for i in range(len(presetFacts)):
    
    rand1 = random.randint(0, presetFacts.__len__()-1)
    #Checks if the fact has been used already
    while(presetFacts[rand1] == None):
        rand1 = random.randint(0, hobbiesAndFacts.__len__()-1)
    

    
    print("Who is associated with ", presetFacts[rand1], "?", sep='')
    
    name = input("Enter the name: ")
    
    if(str.upper(name) == str.upper(names[rand1])):
        points = points + 1
        print("correct")
    else:
        print("Burn in hell", " it was ", names[rand1], sep = "")

    #Removes the fact once it has been used.
    presetFacts[rand1] = None
print("you only got ", points, " points, haha")