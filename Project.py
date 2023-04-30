import datetime
import re
import json
from ansi_color_codes import *

class Project:

    def __init__(self, title, details, target, start_date, end_date, userEmail):
        self.title = title
        self.details = details 
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
        self.userEmail = userEmail


    @staticmethod             
    def createProject(user):
            title = Project.__titleValidation()
            details = Project.__detailsValidation()
            while True:
                target = input(f"{BCyan}Enter target number you want to achieve ==> {Color_Off}")   
                if  (re.search("^\d+$",target)):           
                    target =  int(target)
                    break
                else:
                    print(f"{Red}Target must be a number {Color_Off}")
            while True:
                try:
                    start_date = input(f"{BCyan}Enter start date (yyyy-mm-dd) ==> {Color_Off}")
                    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                    end_date = input(f"{BCyan}Enter end date (yyyy-mm-dd) ==> {Color_Off}")
                    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
                    if(end_date<start_date):
                        raise Exception("End_date must be later than Start_date")
                    else:
                        break
                except Exception as error:
                    print(f"{Red}{error}{Color_Off}")
            project = Project(title,details,target,start_date,end_date,user['email'])
            projectsArr = Project.readProjects()
            Project.addProject(project,projectsArr)


    @staticmethod
    def readProjects():
            projectsArr = []
            with open("projects.json",'r') as file:
                projectsArr = json.load(file)
                file.close()
            return projectsArr


    @staticmethod
    def addProject(project, projectsArr):
            newProject = [{
                "title" : project.title,
                "details": project.details,
                "target": project.target,
                "startDate": str(project.start_date),
                "endDate": str(project.end_date),
                "userEmail": project.userEmail
            }]

            projectsArr.extend(newProject)

            with open("projects.json", 'w') as file:
                json.dump(projectsArr, file, indent=4)
                file.close()
    
    @staticmethod
    def viewProject(user=None, filteredProjects=None):
        projectsArr = []
        with open("projects.json",'r') as file:
                projectsArr = json.load(file)
                file.close()
            
        if(filteredProjects):
            projectsArr = filteredProjects

        border = "+----------------------+----------------------+----------------------+----------------------+----------------------+"
        print(f"{Green}{border}")
        dataTemplate = "| {:<20} | {:<20} | {:<20} | {:<20} | {:<20} |".format('title', 'target', 'start Date', 'end Date', 'userEmail')
        print(dataTemplate)
        print(border)
        for ele in projectsArr:
            dataTemplate = "| {:<20} | {:<20} | {:<20} | {:<20} | {:<20} |".format(ele['title'], ele['target'], ele['startDate'], ele['endDate'], ele['userEmail'])
            print(dataTemplate)
        print(f"{Green}{border}{Color_Off}")


    @staticmethod
    def editProject(user):
        email = user['email']
        projectsArr = Project.readProjects()

        ## filter user projects ##
        filteredProjects = [project for project in projectsArr if project["userEmail"] == email]

        if not filteredProjects:
            print(f"{Red}No projects found for user with email: {email}{Color_Off}")
            return

        print(f"{Yellow}Your projects")
        for i in range(1, len(filteredProjects)+1):
            print(f"{i} - {filteredProjects[i-1]['title']}")
        print(f"{Color_Off}")

        ## select project ##
        while(True):
            projectSelection = input(f"{BCyan}Enter a valid number ==> {Color_Off}")
            try:
                if(not re.search("^[1-9]+0*$", projectSelection)):
                    raise Exception("Enter a valid number")
                if(int(projectSelection) >= len(filteredProjects)+1):
                    raise Exception("Enter a valid number")
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")
            
        projectName = filteredProjects[int(projectSelection)-1]['title']
        print(f"{Green}the selected project is {projectName}{Color_Off}")

        ## select Attribute to edit ##
        attrArr = ['title', 'details', 'target', 'startDate', 'endDate']
        print(f"{Yellow}Attribute Select")
        for i in range(1, len(attrArr)+1):
            print(f"{i} - {attrArr[i-1]}")
        print(f"{Color_Off}")

        while(True):
            attrSelection = input(f"{BCyan}Enter a valid number ==> {Color_Off}")
            try:
                if(not re.search("^[1-9]+0*$", attrSelection)):
                    raise Exception("Enter a valid number")
                if(int(attrSelection) >= len(attrArr)+1):
                    raise Exception("Enter a valid number")
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")
        

        ## Edit Attribute and validation ##
        validationDic = {
            '1': Project.__titleValidation,
            '2': Project.__detailsValidation,
            '3': Project.__targetValidation,
            '4': Project.__startDateValidation,
            '5': Project.__endDateValidation
        }
        for project_to_edit in filteredProjects:
            if(project_to_edit['title'] == projectName):
                project_to_edit[attrArr[int(attrSelection) -1]] = validationDic[attrSelection](project_to_edit)



        # write back to the JSON file
        with open("projects.json", 'w') as file:
                json.dump(projectsArr, file, indent=4)
                file.close()
                print(f"{Green}Projects updated successfully.{Color_Off}")
        
        askAgain = input(f"{BCyan}Want to edit project [y/n] ==> {Color_Off}")
        if(askAgain in ['Y','y']):
            Project.editProject(user)
    

    @staticmethod
    def deleteProject(user):
        print(f"{BBlue}Delete Project{Color_Off}")
        email = user['email']
        projectsArr = Project.readProjects()

        ## filter user projects ##
        filteredProjects = [project for project in projectsArr if project["userEmail"] == email]

        if not filteredProjects:
            print(f"{Red}No projects found for user with email: {email}{Color_Off}")
            return

        print(f"{Yellow}Your projects")
        for i in range(1, len(filteredProjects)+1):
            print(f"{i} - {filteredProjects[i-1]['title']}")
        print(f"{Color_Off}")

        ## select project ##
        while(True):
            projectSelection = input(f"{BCyan}Enter a valid number ==> {Color_Off}")
            try:
                if(not re.search("^[1-9]+0*$", projectSelection)):
                    raise Exception("Enter a valid number")
                if(int(projectSelection) >= len(filteredProjects)+1):
                    raise Exception("Enter a valid number")
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")
            
        projectName = filteredProjects[int(projectSelection)-1]['title']
        print(f"{Green}the selected project is {projectName}{Color_Off}")

        for project_to_edit in filteredProjects:
            if(project_to_edit['title'] == projectName):
                projectsArr.remove(project_to_edit)

        # write back to the JSON file
        with open("projects.json", 'w') as file:
                json.dump(projectsArr, file, indent=4)
                file.close()
                print(f"{Green}The {projectName} project was deleted successfully.{Color_Off}")
        
        askAgain = input(f"{BCyan}Want to delete project [y/n] ==> {Color_Off}")
        if(askAgain in ['Y','y']):
            Project.editProject(user)


    @staticmethod
    def searchOnProject(user):
        print(f"{BBlue}Search on Project by date{Color_Off}\n")

        projectsArr = Project.readProjects()
        ## date selectin (start | end) ##
        dateSearchDir = {'1':'startDate','2':'endDate'}
        print(f"""{Yellow}which date you want to search on
            1 - start date
            2 - end date
            """)
        while(True):
            
            selectionNum = input(f"{BCyan}select a number ==> {Color_Off}")
            try:
                if(not re.search("^[1-9]+0*$", selectionNum) or int(selectionNum) > 2):
                    raise Exception("Enter a valid number\n")
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")
        dateSearch = dateSearchDir[selectionNum]
        ## search condition ##
        conditionDir = {
            '1': Project.__dateIsEqual,
            '2': Project.__dateIsGreater,
            '3': Project.__dateIsLess,
            '4': Project.__dateIsGreaterOrEqual,
            '5': Project.__dateIsLessOrEqual 
        }
        print(f"""{Yellow}the {dateSearch} .... entered date
            1 - equal to
            2 - greater than
            3 - less than
            4 - greater than or equal
            5 - less than or equal
            """)
        while(True):
            
            selectionNum = input(f"{BCyan}select a number ==> {Color_Off}")
            try:
                if(not re.search("^[1-9]+0*$", selectionNum) or int(selectionNum) > 5):
                    raise Exception("Enter a valid number\n")
                
                conditionDir[selectionNum](projectsArr, dateSearch)
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")   

    @staticmethod
    def __titleValidation(project=None):
        
        while(True):
            data = input(f"{BCyan}Enter a title ==> {Color_Off}")
            try:
                if(not data):
                    raise Exception(f"{Red}Empty title not valid{Color_Off}")
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")
        return data


    @staticmethod
    def __detailsValidation(project=None):
        
        while(True):
            data = input(f"{BCyan}Enter the details ==> {Color_Off}")
            try:
                if(not data):
                    raise Exception(f"{Red}Empty details not valid{Color_Off}")
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")
        return data


    @staticmethod
    def __targetValidation(project=None):
        
        while(True):
            data = input(f"{BCyan}Enter the target money ==> {Color_Off}")
            try:
                if(not re.search("^\d+$", data)):
                    raise Exception(f"{Red}Target should be a number{Color_Off}")
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")
        return int(data)

    
    @staticmethod
    def __startDateValidation(project=None):

        while(True):
            startDate = input(f"{BCyan}Enter start date as [yyyy-mm-dd] ==> {Color_Off}")
            try:
                startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
                if(project):
                    dateStr = project['endDate'].split()[0]
                    projectEndDate = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
                if(startDate > projectEndDate):
                    raise Exception(f"{Red}Start date is after end date{Color_Off}")
            
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")

        return str(startDate)


    @staticmethod
    def __endDateValidation(project=None):
        
        while(True):
            endDate = input(f"{BCyan}Enter the end date as [yyyy-mm-dd] ==> {Color_Off}")
            try:
                endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
                if(project):
                    dateStr = project['startDate'].split()[0]
                    projectStartDate = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
                if(endDate < projectStartDate):
                    raise Exception(f"{Red}End date is before start date{Color_Off}")
            
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}")

        return str(endDate)
    
    @staticmethod
    def __dateIsEqual(projectsArr, dateSearch):
        
        while(True):
            date = input(f"{BCyan}Enter the date as [yyyy-mm-dd] ==> {Color_Off}")
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}\n")

        filteredProjects = [project for project in projectsArr 
                            if datetime.datetime.strptime(project[dateSearch].split()[0], '%Y-%m-%d') == date]
        if(not filteredProjects):
            print(f"{Red}No project with that date{Color_Off}")
            return
        Project.viewProject(filteredProjects= filteredProjects)

    @staticmethod
    def __dateIsGreater(projectsArr, dateSearch):
        
        while(True):
            date = input(f"{BCyan}Enter the date as [yyyy-mm-dd] ==> {Color_Off}")
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}\n")

        filteredProjects = [project for project in projectsArr 
                            if datetime.datetime.strptime(project[dateSearch].split()[0], '%Y-%m-%d') > date]
        if(not filteredProjects):
            print(f"{Red}No project with that date{Color_Off}")
            return
        Project.viewProject(filteredProjects= filteredProjects)       
    

    @staticmethod
    def __dateIsLess(projectsArr, dateSearch):
        
        while(True):
            date = input(f"{BCyan}Enter the date as [yyyy-mm-dd] ==> {Color_Off}")
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}\n")

        filteredProjects = [project for project in projectsArr 
                            if datetime.datetime.strptime(project[dateSearch].split()[0], '%Y-%m-%d') < date]
        if(not filteredProjects):
            print(f"{Red}No project with that date{Color_Off}")
            return 
        Project.viewProject(filteredProjects= filteredProjects)

    @staticmethod
    def __dateIsGreaterOrEqual(projectsArr, dateSearch):
        
        while(True):
            date = input(f"{BCyan}Enter the date as [yyyy-mm-dd] ==> {Color_Off}")
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}\n")

        filteredProjects = [project for project in projectsArr 
                            if datetime.datetime.strptime(project[dateSearch].split()[0], '%Y-%m-%d') >= date]
        if(not filteredProjects):
            print(f"{Red}No project with that date{Color_Off}")
            return                    
        Project.viewProject(filteredProjects= filteredProjects)


    @staticmethod
    def __dateIsLessOrEqual(projectsArr, dateSearch):
        
        while(True):
            date = input(f"{BCyan}Enter the date as [yyyy-mm-dd] ==> {Color_Off}")
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                break
            except Exception as err:
                print(f"{Red}{err}{Color_Off}\n")

        filteredProjects = [project for project in projectsArr 
                            if datetime.datetime.strptime(project[dateSearch].split()[0], '%Y-%m-%d') <= date]
        if(not filteredProjects):
            print(f"{Red}No project with that date{Color_Off}")
            return
        Project.viewProject(filteredProjects= filteredProjects)     














 
