import getpass
import sys
from time import sleep
from essentials import *
import os
import routines

global username
username = getpass.getuser().upper()

#saveInfo Key
#==================
#line 1 - opening
#line 2 - Logic Skill
#line 3 - Math Skill
#line 4 - Communication Skill
#line 5 - Analytics Skill
#line 6 - Intimidation Skill
#line 7 - Business Skill
#line 8 - Creativity Skill
#line 9 - Literacy Skill
#line 10 - Artwork Skill

fName = open("saveInfo.txt","r")
fContent = fName.read().split("\n")
fName.close()


def opening():
  newPrint("HELLO, "+username)
  sleep(1)
  newPrint("WELCOME TO YOUR NEW COMPUTATIONAL INTERCONNECTION DEVICE! THE FUTURE IS HERE!")
  newPrint("WE HAVE INCLUDED A MANUAL TO HELP YOU GET STARTED.")
  newPrint("YOU CAN OPEN THE MANUAL BY TYPING '-E MANUAL' IN THE CONSOLE.")
  newPrint("THANK YOU FOR BUYING FROM")
  newPrint("N E W  T E C H")
  sleep(3)
  os.system("cls")

if fContent[0] == "false":
  opening()
  writeSave("true",0)
 

while True:
  userInput = input("\nO://USERMAIN >> ")
  if userInput.upper() == "MANUAL":
    routines.userManual()
  elif userInput.upper() == "SCHOOL":
    routines.school()
  else:
    newPrint("INPUT INVALID. PLEASE RE-ENTER.")
