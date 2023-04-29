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
    def createProject(user):
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
    def viewProject(user):
            projectsArr = []
            with open("projects.json",'r') as file:
                    projectsArr = json.load(file)
                    file.close()
                    print(json.dumps(projectsArr, indent=4))
            


     

    @staticmethod
    def editProject(user):
        email = user['email']
        projectsArr = Project.readProjects()

        filteredProjects = [project for project in projectsArr if project["userEmail"] == email]

        if not filteredProjects:
            print("No projects found for user with email:", email)
            return

        value_to_be_edited = input("Enter the key to be edited (title/details/target/start_date/end_date): ")
        new_value = input("Enter new value: ")

        for project_to_edit in filteredProjects:
            if value_to_be_edited not in project_to_edit:
                print("Invalid key entered for project:", project_to_edit['title'])
                continue

        project_to_edit[value_to_be_edited] = new_value

        # write back to the JSON file
        with open("projects.json", 'w') as file:
                json.dump(projectsArr, file, indent=4)
                file.close()
                print("Projects updated successfully.")


user = {
        "firstName": "mona",
        "lastName": "ahmed",
        "email": "mona@gmail.com",
        "password": "$2b$12$4UOIpQAakX0ptcH5MVwKiOeZQ1LWtKRc49z6R/YTigGwo4FtC4ggu",
        "mobile": "01012345678"
        }                 
#print(Project.createProject())


#print(Project.viewProject())

print(Project.editProject(user))













 
