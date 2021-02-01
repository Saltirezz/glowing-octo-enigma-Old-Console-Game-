import sys
from time import sleep
import os
def newPrint(words):
    sys.stdout.write("\n")
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
def readSave(linesLower, linesUpper):
    readList = []
    fName = open("saveInfo.txt","r")
    for i, line in enumerate(fName):
        if i > linesLower and i < linesUpper:
            line = line.rstrip()
            readList.append(line)
    fName.close()
    return readList
def writeSave(writeContent,index):
    fName = open("saveInfo.txt","r")
    fContent = fName.readlines()
    fName = open("saveInfo.txt","w")
    fContent[index] = writeContent+"\n"
    fName.writelines(fContent)
    fName.close()
def readIntoArray(path,splitLines):
    fName = open(path,"r")
    array = fName.read().splitlines(splitLines)
    fName.close()
    return array
def classCountdown():
    newPrint("GET READY. . .\n")
    sleep(2)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("GO!")
    os.system("cls")
def readFile(path):
    fName = open(path,"r")
    fContent = fName.readlines()
    fName.close()
    return fContent

