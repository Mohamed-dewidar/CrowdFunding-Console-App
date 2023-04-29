import datetime
import re
import json
class Project:
    def __init__(self, title, details, target, start_date, end_date):
        self.title = title
        self.details = details 
        self.target = target
        self.start_date = start_date
        self.end_date = end_date


    @staticmethod             
    def createProject():
            title = input("Enter project title: ")
            details = input("Enter project details: ")
            while True:
                target = input("Enter target number you want to achieve: ")   
                if  (re.search("^\d+$",target)):           
                    target =  int(target)
                    break
                else:
                    print("Target must be a number ")
            while True:
                try:
                    start_date = input("Enter start date (yyyy-mm-dd): ")
                    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                    end_date = input("Enter end date (yyyy-mm-dd): ")
                    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
                    if(end_date<start_date):
                        raise Exception("End_date must be later than Start_date")
                    else:
                        break
                except Exception as error:
                    print(error)
            project1 = Project(title,details,target,start_date,end_date)
            projectsArr = Project.readProjects()
            Project.addProject(project1,projectsArr)




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
                "endDate": str(project.end_date)
            }]

            projectsArr.extend(newProject)

            with open("projects.json", 'w') as file:
                json.dump(projectsArr, file, indent=4)
                file.close()
    
    @staticmethod
    def viewProject():
            projectsArr = []
            with open("projects.json",'r') as file:
                    projectsArr = json.load(file)
                    file.close()
                    return json.dumps(projectsArr, indent=4)

    @staticmethod
    def editProject():
            projectsArr = []
            with open("projects.json",'r') as file:
                    projectsArr = json.load(file)
                    file.close()
                    return projectsArr
  



#print(Project.createProject())


#print(Project.viewProject())

#print(Project.editProject())













 