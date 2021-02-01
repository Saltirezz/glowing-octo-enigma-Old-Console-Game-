from essentials import *
from time import sleep
import time
import random
import os
import operator

def programmingClass(level):
    #question setup
    letters = ("A","B","C","D")
    possibleAnswers = []
    #amount of questions for each level
    questionAmount = [2,0,0,0,0,0,0,0,0,0]
    #getting the question and solutions
    curQuestionIndex = random.randrange(1,questionAmount[level-1]+1)
    curQuestion = readIntoArray("programmingClassProblems/"+str(level)+"/"+str(curQuestionIndex)+".txt",False)
    solutionIndex = curQuestion.pop(-1)
    curQuestion = '\n'.join(curQuestion)
    
    #getting the solution and 3 other random solutions
    fContent = readIntoArray("programmingClassProblems/answerList.txt",False)
    possibleAnswers.append(fContent.pop(int(solutionIndex)-1))
    answerKey = possibleAnswers[0]
    #add the answers to array
    for i in range(1,4):
        possibleAnswers.append(fContent.pop(random.randrange(0,len(fContent))))
    #randomize and add a,b,c,d at the start
    random.shuffle(possibleAnswers)
    for i in range(0,4):
        #getting the correct solutions position in the answers
        if possibleAnswers[i] == answerKey:
            answerLetter = letters[i]
        possibleAnswers[i] = letters[i]+"."+possibleAnswers[i]
    possibleAnswers = '\n'.join(possibleAnswers)


    ticks = 0
    #countdown
    print("PROGRAMMING CLASS.")
    newPrint("WELCOME TO PROGRAMMING CLASS.")
    newPrint("YOU WILL BE PRESENTED WITH CODE AND MUST ANSWER WITH WHAT THE CODE WILL DO.")
    sleep(1)
    classCountdown()
    while ticks <= 20*level:
        sleep(1)
        ticks += 1
        print("SOLVE THIS. \n")
        print(curQuestion)
        print("")
        print(possibleAnswers)
        userAnswer = input("WHAT ONE IS IT ('A','B','C' or 'D'): ")
        if userAnswer.upper() == answerLetter:
            newPrint("YOU HAVE PASSED THIS CLASS.")
            os.system("cls")
            return True
            break
        else:
            newPrint("YOU HAVE FAILED THIS CLASS.")
            os.system("cls")
            return False
            break
def mathClass(level):
    answer = []
    user = []
    amountCorrect = 0
    newPrint("WELCOME TO MATH CLASS.")
    newPrint("YOU WILL HAVE TO SOLVE 10 MATH PROBLEMS.\n")
    classCountdown()
    operators = [('+', operator.add),('-', operator.sub),('*',operator.mul)]
    for i in range(0,10):
        a = (level)*(random.randint(1, 10))
        b = (level)*(random.randint(1, 10))
        op, fn = random.choice(operators)
        answer.append(fn(a, b))
        user.append(input("{} {} {} = ".format(a, op, b)))
        if int(user[i]) == answer[i]:
            amountCorrect += 1
    if amountCorrect >= 8:
        newPrint("YOU HAVE PASSED THIS CLASS.\n")
        return True
    else:
        newPrint("YOU HAVE FAILED THIS CLASS.\n")
        return False
def literacyClass(level):
    ticks = 0
    newPrint("WELCOME TO LITERACY CLASS.")
    newPrint("YOU WILL HAVE TO REPLICATE A GIVEN TEXT.\n")
    if level <=3:
        #easy file
        fileContent = readIntoArray("literacyClass/Easy.txt",False)
    elif level <= 6:
        #medium file
        fileContent = readIntoArray("literacyClass/Medium.txt",False)
    elif level <= 9:
        #hard file
        fileContent = readIntoArray("literacyClass/Hard.txt",False)
    else:
        #very hard file
        fileContent = readIntoArray("literacyClass/VeryHard.txt",False)
    question = random.choice(fileContent)
    solution = question.replace("\n"," ")
    classCountdown()
    print(question)
    userAnswer = input("TYPE INPUT HERE: ")
    if userAnswer == solution:
        newPrint("YOU HAVE PASSED THIS CLASS.\n")
        return True
    else:
        newPrint("YOU HAVE FAILED THIS CLASS. \n")
        return False
def artClass(level):
    newPrint("YOU WILL CREATE PICTURES USING THE INSTRUCTIONS GIVEN.")
    newPrint("SYNTAX FOR THESE INSTRUCTIONS CAN BE FOUND BY TYPING IN 'HELP'.")
    questions = readIntoArray("artClass/Questions.txt",False)
    solutions = readIntoArray("artClass/Solutions.txt",False)
    questionIndex = random.randrange(0,len(questions)-1)
    classCountdown()
    print(questions[questionIndex])
    while True:
        userInput = input("\nENTER INPUT: ")
        if userInput.upper() == "HELP":
            print("AT THE START YOU SHOULD ALWAYS SPECIFY HOW BIG THE GRID IS. KEEP IN MIND THAT THE GRID IS CALCULATED LEFT TO RIGHT SO THE MIDDLE OF A 5X5 GRID IS BOX 12.")
            print("AN INSTRUCTION CAN LOOK LIKE THIS - ")
            print("5:12:LINES:4:0:180:0:180:BLACK")
            print("THAT WAS A BASIC SQUARE. THE GRID IS 5X5:ITS GRID POSITION IS THE 12 BOX:IT HAS LINES:4 LINES:TOP LINE ROTATION:RIGHT LINE ROTATION:BOTTOM LINE ROTATION:LEFT LINE ROTATION:COLOUR FILLE THIS SHAPE BALCK")
            print("ONLY USE THE NUMBER OF COMMANDS THAT YOU NEED. A LIST OF COMMANDS CAN BE FOUND AT THE BOTTOM OF THIS HELP GUIDE.")
            print("GRID POSITION:LINES OR NOT:IF IT HAS LINES THEN HOW MANY:THE ROTATION OF LINES(THIS IS REPEATED FOR HOWEVER MANY LINES YOU HAVE:IF IT DOESNT HAVE LINES WHAT IS IT'S RADIUS:IF NO LINES HOW MANY DEGREES DOES THIS SHAPE REVOLVE:SHOULD THIS SHAPE BE FILLED WITH COLOUR:COLOUR")
            print("IF THERE ARE MULTPIPLE SHAPES TO CREATE, SEPERATE THE SHAPES WITH '&'. SO COMMANDS:COMMANDS:COMMANDS & COMMANDS:COMMANDS:COMMANDS")
            print("SYNTAX IS VERY IMPORTANT AND ERRORS ARE FATAL. BE CAREFUL WITH WHAT YOU TYPE.")
        else:
            if userInput == solutions[questionIndex]:
                newPrint("YOU HAVE PASSED THIS CLASS.")
                return True
            else:
                newPrint("YOU HAVE FAILED THIS CLASS.")
                return False

        
           
            