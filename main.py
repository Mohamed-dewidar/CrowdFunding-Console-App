from User import User
from Project import Project
from ansi_color_codes import *
import re
import json
import sys

print(f"{Blue} Crowdfunding App {Color_Off}")


def mainHome():

    print(f"""{BBlue}
###############
## Main Home ##    
###############
    {Yellow}
    1 - Register
    2 - login
    {Color_Off}""")

    menuSelection = {
        '1': User.register,
        '2': User.login,
        '3': projectMenu
    }

    while(not User.currUser):
        num = input(f"{BCyan}Enter a selection number ==> {Color_Off}")
        try:
            if(menuSelection[num]):
                menuSelection[num]()
        except Exception as err:
            print(f"{Red}Enter a valin choice{Color_Off}")

    print(f"{BGreen}Welcome {User.currUser['firstName']}{Color_Off}\n")
    projectMenu() 



def projectMenu():

    print(f"""{BBlue}
##################
## Project Menu ##    
##################
    {BYellow}
    1 - add project
    2 - list all projects
    3 - edit project
    4 - search for project by date
    {Color_Off}""")


    menuSelection = {
        '1': Project.createProject
    }

    while(True):
        num = input(f"{BCyan}Enter a selection number ==> {Color_Off}")
        try:
            if(menuSelection[num]):
                menuSelection[num]()
                break
        except Exception as err:
            print(f"{Red}Enter a valin choice{Color_Off}")    



mainHome()




  