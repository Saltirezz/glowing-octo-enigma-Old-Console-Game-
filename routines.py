from essentials import *
from schoolClasses import *

def userManual():
    userInput = ""
    manualCommands = (("SCHOOL","LEARN SKILLS WHICH CAN HELP YOU GET A JOB."),("COMMAND2","ALSO DOES SOMETHING BUT ALSO DUNNO WHAT THOUGH"),("COMMAND3","WHAT AM I EVEN DOING ANYMORE"),("COMMAND4","OKAY, THESE DESCRIPTIONS ARE GETTING RIDICULOUS"))
    longestDesc = [manualCommands[0][0],manualCommands[0][1]]
    #descriptions will always be x spaces away from names.
    defaultSpacing = " "*20
    spacing = 0
    #figure out spacing so descriptions align perfectly, and then output names and descriptions
    for i in manualCommands:
        if len(i[0]) > len(longestDesc[0]):
            longestDesc[0] = i[0]
        if len(i[1]) > len(longestDesc[1]):
            longestDesc[1] = i[1] 
    for i in manualCommands:
        spacing = " "*((len(longestDesc[1]) - len(i[1])) +(len(longestDesc[0]) - len(i[0])))
        print(i[0]+defaultSpacing+spacing+i[1])
def school():
    #basically a case statement but in python, look at the input loop to see what i'm doing.
    classesSwitchCase = {
        1: programmingClass,
        2: mathClass,
        3: literacyClass,
        4: artClass
    }
    #0 = logic, 1 = math, 2 = communication, 3 = analytics, 4 = intimidation, 5 = business, 6 = creativity, 7 = literacy, 8 = artwork
    skillsList = readSave(0,10)
    #0 = class name, 1 = requirementsText, 2 = description
    classes = [["1.PROGRAMMING CLASS "+skillsList[0], "LOGIC LEVEL "+skillsList[0], "TRAIN YOUR LOGIC WITH A PROGRAMMING CLASS."],
               ["2.MATH CLASS "+skillsList[1], "MATH LEVEL "+skillsList[1], "YOU WILL LEARN TO DO 1+1."],
               ["3.LITERACY CLASS"+skillsList[2],"LITERACY LEVEL "+skillsList[2], "BRUSH UP ON YOUR ABC'S."],
               ["4.ART CLASS"+skillsList[3],"ART LEVEL "+skillsList[3], "LEARN TO DRAW."]]

    newPrint("WELCOME TO SCHOOL. WHAT WOULD YOU LIKE TO LEARN?")
    print("(CLASS NAME:SKILL REQUIREMENT:CLASS DESCRIPTION)")
    longestStuff = [classes[0][0],classes[0][1],classes[0][2]]
    defaultSpacing = " "*8
    spacing = [0,0]
    #this is meant to space like the usermanual but doenst work. FIX!!
    for i in classes:
        if len(i[0]) > len(longestStuff[0]):
            longestStuff[0] = i[0]
        if len(i[1]) > len(longestStuff[1]):
            longestStuff[1] = i[1]
        if len(i[2]) > len(longestStuff[2]):
            longestStuff[2] = i[2]
    for i in classes:
        spacing[0] = " "*((len(longestStuff[1]) - len(i[1])) +(len(longestStuff[0]) - len(i[0])))
        spacing[1] = " "*(len(longestStuff[2]) - len(i[2]))
        print(i[0]+defaultSpacing+spacing[0]+i[1]+defaultSpacing+spacing[1]+i[2])
    #input loop
    while True:
        userInput = input("CHOOSE A CLASS BY ENTERING ITS NUMBER. (TO LEAVE SCHOOL TYPE 'EXIT')")
        if userInput.upper() == "EXIT":
            break
        elif userInput.isnumeric() and int(userInput) >= 1 and int(userInput) <= len(classes):
            func = classesSwitchCase.get(int(userInput), lambda: "INVALID INPUT")
            func(int(skillsList[int(userInput)-1]))
        else:
            newPrint("INPUT INVALID. PLEASE RE-ENTER")


   
    