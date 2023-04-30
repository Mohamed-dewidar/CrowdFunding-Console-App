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
    3 - exit
    {Color_Off}""")

    menuSelection = {
        '1': User.register,
        '2': User.login
    }

    while(not User.currUser):
        num = input(f"{BCyan}Enter a selection number ==> {Color_Off}")
        try:
            if(num == '3'):
                sys.exit()
            if(menuSelection[num]):
                menuSelection[num]()
        except Exception as err:
            print(f"{Red}Enter a valin choice{Color_Off}")

    print(f"{BGreen}Welcome {User.currUser['firstName']}{Color_Off}\n")
    projectMenu() 



def projectMenu():
    
    menuSelection = {
        '1': Project.createProject,
        '2': Project.viewProject,
        '3': Project.editProject,
        '4': Project.deleteProject,
        '5': Project.searchOnProject
    }

    while(True):
        print(f"""{BBlue}
##################
## Project Menu ##    
##################{Color_Off}  
        {BYellow}
    1 - add project
    2 - list all projects
    3 - edit project
    4 - delete project
    5 - search for project by date
    6 - Log out
    7 - exit
    {Color_Off}""")

        num = input(f"{BCyan}Enter a selection number ==> {Color_Off}")
        try:
            if(num == '7'):
                sys.exit()
            if(num == '6'):
                User.currUser = None
                mainHome()
                return
            if(menuSelection[num]):
                menuSelection[num](User.currUser)
        except Exception as err:
            print(f"{Red}Enter a valid choice{Color_Off}")    
    
  




## App Start ##
mainHome()




  