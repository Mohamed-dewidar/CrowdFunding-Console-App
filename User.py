from ansi_color_codes import *
import json
import re
import bcrypt

class User:
    currUser = None
    def __init__(self, firstName: str, lastName: str, email: str, password: str, mobile: str) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.mobile = mobile

    @staticmethod
    def register() -> object:
        print(f"{BBlue}\nRegisteration{Color_Off}")
        fName, lName = User.__nameValidation()
        email = User.__emailValidation()
        passwordHash = User.__passwordValidation()
        mobile = User.__mobileValidation()

        user = User(fName, lName, email, passwordHash, mobile)
        
        userArr = User.readUsers()
        User.addUser(user, userArr)
        User.login()
        

    @staticmethod
    def __nameValidation() -> None:
        nameRegex = "^[a-zA-Z]+$"

        fName = input(f"{BCyan}Enter your First Name, lowercase & uppercase letters ==> {Color_Off}")
        while (not re.search(nameRegex, fName)):
                print(f"{Red}Enter a valid Name{Color_Off}")
                fName = input(f"{BCyan}Enter your First Name, lowercase & uppercase letters ==> {Color_Off}")

        lName = input(f"{BCyan}Enter your Last Name, lowercase & uppercase letters ==> {Color_Off}")
        while (not re.search(nameRegex, lName)):
                print(f"{Red}Enter a valid Name{Color_Off}")
                lName = input(f"{BCyan}Enter your Last Name, lowercase & uppercase letters ==> {Color_Off}")
 
        return fName, lName
            

    @staticmethod
    def __emailValidation() -> None:
        emailRegex = "^[\w]+@([\w-]+\.)+[\w-]{3}$"

        email = input(f"{BCyan}Enter email ==> {Color_Off}")
        while (not re.search(emailRegex, email)):
            print(f"{Red}Enter a valid Email{BCyan}")
            email = input(f"{BCyan}Enter email ==> {Color_Off}")

        return email

    @staticmethod
    def __passwordValidation() -> None:
        passwordRegex = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

         
        password = input(f"""{BCyan}password contains at least 8 characters
            - 1 uppercase letter
            - 1 lowercase letter
            - 1 number
            - 1 special
            Enter Password ==> {Color_Off}""")

        while (not re.search(passwordRegex, password)): 
            print(f"{Red}Enter a valid Password{Color_Off}")
            password = input(f"""{BCyan}password contains at least 8 characters
            - 1 uppercase letter
            - 1 lowercase letter
            - 1 number
            - 1 special
            Enter Password ==> {Color_Off}""")


        confirmPass = input(f"{BCyan}Confirm Password ==> {Color_Off}")
        while(not password == confirmPass):
            print(f"{Red}Passwords does not match{Color_Off}")
            confirmPass = input(f"{BCyan}Confirm Password ==> {Color_Off}")

        passwordHash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        return passwordHash.decode("utf-8")


    @staticmethod
    def __mobileValidation() -> None:
        mobileRegex = "^01[0125][\d]{8}$"

        mobile = input(f"{BCyan}Enter Mobile ==> {Color_Off}")
        while(not re.search(mobileRegex, mobile)):
            print(f"{Red}Enter a valid mobile number")
            mobile = input(f"{BCyan}Enter Mobile ==> {Color_Off}")

        return mobile


    @staticmethod
    def login() -> object:
        print(f"{BBlue}\nLogin{Color_Off}")
        emailRegex = "^[\w]+@([\w-]+\.)+[\w-]{3}$"
        passwordRegex = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

        email = input(f"{BCyan}Enter email ==> {Color_Off}")
        while (not re.search(emailRegex, email)):
            print(f"{Red}Enter a valid Email{BCyan}")
            email = input(f"{BCyan}Enter email ==> {Color_Off}")



        password = input(f"""{BCyan}Enter Password ==> {Color_Off}""")
        while (not re.search(passwordRegex, password)): 
            print(f"{Red}Enter a valid Password{Color_Off}")
            password = input(f"""{BCyan}Enter Password ==> {Color_Off}""")

        usersArr = User.readUsers()
        for user in usersArr:
            if(email == user['email'] and  bcrypt.checkpw(password.encode("utf-8"), user['password'].encode("utf-8") )):
                User.currUser = user
                return
            
        print(f"{Red}Login data is wrong{Color_Off}")
        userRes = input(f"{BCyan} back to register [Y/N] ==> {Color_Off}")
        while(not userRes in ['Y','y','N','n']):
            print(f"{Red}Enter a valid option{Color_Off}")
            userRes = input(f"{BCyan} back to register [Y/N] ==> {Color_Off}")
        
        if(userRes in ['y','Y']):
            User.register()
        else:
            User.login()

    @staticmethod
    def readUsers():
        usersArr = []
        with open("users.json",'r') as file:
            usersArr = json.load(file)
            file.close()
        return usersArr
    
    @staticmethod
    def addUser(user, usersArr):
        newuser = [{
            "firstName" : user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "password": user.password,
            "mobile": user.mobile
        }]
        
        usersArr.extend(newuser)
       
        with open("users.json", 'w') as file:
            json.dump(usersArr, file, indent=4)
            file.close()
            
            




     