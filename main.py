import random
import time
import string
import pyperclip
import os.path
from time import sleep


def initalSetup():
    print("Hello, Welcome to ToesManager, a Local Password Manager!")
    sleep(1)
    print("Lets start by you name!")
    usersName = input(": ")
    print("Great!")
    sleep(1)
    print("Now, create a master password to access all you password!")
    sleep(1)
    masterPassword = input(": ")

    print("Are These Correct?")
    print(usersName)
    print(masterPassword)
    askIfCorrect = input(": ").upper()
    
    while askIfCorrect != "YES":
        print("What would you like to change?")
        askWhatToChange = input("Name or Password or Both: ").upper()
        if askWhatToChange == "NAME":
            print("Please enter in you name.")
            usersName = input(": ")
        elif askWhatToChange == "PASSWORD":
            print("Please enter in your master Password again!")
            masterPassword = input(":")
        elif askWhatToChange == "BOTH":
            print("Please enter in you name.")
            usersName = input(": ")
            print("Please enter in your master Password again!")
            masterPassword = input(":")
        else:
            print("Please say YES or NO or BOTH")
            
        print("Are These Correct?")
        print(usersName)
        print(masterPassword)
        askIfCorrect = input(": ").upper()
    
    with open ("usersName.txt", "w") as usersNameFile:
        usersNameFile.write(usersName)
        usersNameFile.close()
    with open ("masterPassword.txt", "w") as usersPasswordFile:
        usersPasswordFile.write(masterPassword)
        usersPasswordFile.close()        

checkForFile1 = (os.path.exists("usersName.txt"))
checkForFile2 = (os.path.exists("masterPassword.txt"))
if checkForFile1 and checkForFile2 == True:
    pass
else:
    initalSetup()


with open("usersName.txt", "r") as readUsersName:
    nameOfUser = readUsersName.readline()
with open("masterPassword.txt", "r") as readMasterPassword:
    usersMasterPasswd = readMasterPassword.readline()

password_tries = 0 
while password_tries < 3:

    enter_password = input("Enter Password: ")
    right_password = usersMasterPasswd
    quit_password = "QUIT"
    password_tries += 1

    if enter_password == right_password:

        while True:
            command = input("How can I help you today?: ").upper()
    
            if command == "NEW":
                name_of_software = input("Enter the web or app name: ")
                username = input("Enter your username: ") 
                try:
                    input_length = int(input("Enter the length: "))
                except ValueError:
                    print("Try entering an interger")
                    continue

                speical_Letters = "!@#$%^&*_+=-~`<>/?()"
                contentsOfPassword = string.ascii_uppercase + string.ascii_lowercase + string.digits + speical_Letters

                Password = "".join(random.sample(contentsOfPassword, input_length))

                print(Password)

                askIfNeedtoCopy = input("Do you want it to be copy to the clipboard? (Y/N): ").upper()
                if askIfNeedtoCopy == "Y":
                    pyperclip.copy(Password)
                else:
                    print("Alright then.")

                   
                print("Aight bet.")

                with open("Passwords.txt", "a") as writePasswordtoFile:
                    writePasswordtoFile.write(f"{name_of_software}: \nUserName:\n    {username}\nPassword:\n    {Password}\n\n")
                    writePasswordtoFile.close()

            elif command == "ADD":
                add_appName = input("Enter the Website or App: ")
                add_userName = input("Enter the username for it: ")
                
                while True:
                    add_passWord = input("Enter the password for it: ")
                    add_passWord_Verify = input("Verify your password: " )

                    if add_passWord == add_passWord_Verify:
                        with open("Passwords.txt" , "a") as addPasswords:
                            addPasswords.write(f"{add_appName}: \nUserName:\n    {add_userName}\nPassword:\n    {add_passWord}\n\n")
                            addPasswords.close()

                        print("Sucess!")
                        break
                    
                    elif add_passWord != add_passWord_Verify:
                        print("Try again.")
                        continue

            elif command == "CHECK":
                with open("Passwords.txt", "r") as readPasswordFile:
                    print(readPasswordFile.read())
                    readPasswordFile.close()

            elif command == "QUIT":
                print("Closing...")
                time.sleep(2)
                quit()

            else:
                print("Wrong thing mate")

    elif enter_password.upper() == quit_password:
        print("Closing...")
        time.sleep(2)
        break

    else:
        print(f'You are not {nameOfUser} You muffiinHead!!!')

else:
    print("User Authtication Failed")
    print("quiting...")
    time.sleep(2)
    quit()


