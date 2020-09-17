import random
import time
import string
import pyperclip
import os.path
from time import sleep
from function import clear
import time
import getpass

class ToesManager:
    
  def Inital_Setup():
    print("Hello, Welcome to ToesManager, a Local Password Manager!")
    sleep(1)
    print("Lets start by you name!")
    usersName = input(": ")
    print("Great!")
    sleep(1)
    print("Now, create a master password to access all you password!")
    sleep(1)
    # masterPassword = input(": ")
    masterPassword = getpass.getpass(": ")

    print("Are These Correct?")
    print(usersName)
    print(masterPassword)
    askIfCorrect = input("(YES/NO): ").upper()
    
    while askIfCorrect != "YES":
      print("What would you like to change?")
      askWhatToChange = input("Name or Password or Both: ").upper()
      if askWhatToChange == "NAME":
        print("Please enter in you name.")
        usersName = input(": ")
      elif askWhatToChange == "PASSWORD":
        print("Please enter in your master Password again!")
        # masterPassword = input(":")
        masterPassword = getpass.getpass(": ")
      elif askWhatToChange == "BOTH":
        print("Please enter in you name.")
        usersName = input(": ")
        print("Please enter in your master Password again!")
        # masterPassword = input(":")
        masterPassword = getpass.getpass(": ")
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

    print("Welcome,\n here is some commands that you might need")
    print('''
    New - Generate a new password
    Add - Add a password that already exists
    Check - Check all the password that the user stored
    Quit - Quit the program
    Clear - Clears the console
    Help - List all command
    ''')

    sleep(2)

  def Generate_Password():
    name_of_software = input("Enter the web or app name: ")

    if name_of_software.upper() == "BACK":
      return
    else:
      pass

    if name_of_software.upper() == "EXIT" or "QUIT":
      ToesManager.Quiting_Program()
    else:
      pass

    username = input("Enter your username: ")
    while True: 
      try:
        input_length = int(input("Enter the length: "))
        break
      except ValueError:
        print("Try entering an interger")
        continue


    speical_Letters = "!@#$%^&*_+=-~`<>/?()"
    contentsOfPassword = string.ascii_uppercase + string.ascii_lowercase + string.digits + speical_Letters

    Password = "".join(random.sample(contentsOfPassword, input_length))

    print(Password)
    pyperclip.copy(Password) 
    print("The password is created and Copied!")

    with open("Password.txt", "a") as writePasswordtoFile:
      writePasswordtoFile.write(f"{name_of_software}: \nUserName:\n    {username}\nPassword:\n    {Password}\n\n")
      writePasswordtoFile.close()


  def Add_Password():
    add_appName = input("Enter the Website or App: ")
    if add_appName.upper() == "BACK":
      return
    else:
      pass
    add_userName = input("Enter the username for it: ")

    if add_appName.upper() == "EXIT" or "QUIT":
      ToesManager.Quiting_Program()
    else:
      pass
    
    while True:
      # add_passWord = input("Enter the password for it: ")
      # add_passWord_Verify = input("Verify your password: " )

      add_passWord = getpass.getpass("Enter the password for it: ")
      add_passWord_Verify = getpass.getpass("Verify your password: ")

      if add_passWord == add_passWord_Verify:
        with open("Password.txt" , "a") as addPassword:
          addPassword.write(f"{add_appName}: \nUserName:\n    {add_userName}\nPassword:\n    {add_passWord}\n\n")
          addPassword.close()

          print("Sucess!")
          break
      
      elif add_passWord != add_passWord_Verify:
        print("Try again. The password doesn't match")
        continue
      else:
        print("Enter in a password!")


  def Check_Password():
    with open("PasswordFixed Bug Clear in Windows.txt", "r") as readPasswordFile:
      print(readPasswordFile.read())
      readPasswordFile.close()


  def Quiting_Program():
    print("Closing...")
    sleep(2)
    quit()

  def Help():
    print("These are the avalible commands")
    print('''
    New - Generate a new password
    Add - Add a password that already exists
    Check - Check all the password that the user stored
    Quit - Quit the program
    Clear - Clears the console
    Help - List all command
    ''')

  def Clear_Console():
      clear.Clear_Console()

  # def tess():
  #     global startlog
  #     if time.time() - 5 > startlog:
  #         print('its been 20 secs')
  #         startlog = time.time()

  def Change_Settings():
    print("What settings do you want to change?")
    print("Username or Password?")
    Change_setting_anwser = input(": ").upper()

    if Change_setting_anwser == "PASSWORD":
      print("Enter in your new password!")
      # Users_New_Password = input(": ")
      Users_New_Password = getpass.getpass(": ")
      with open("masterPassword.txt", "w") as Change_password_file:
        Change_password_file.write(Users_New_Password)
      print("Sucess!")

    elif Change_setting_anwser == "USERNAME":
      print("Enter in your new username!")
      Users_New_Username = input(": ")
      with open("usersName.txt", "w") as Change_name_file:
        Change_name_file.write(Users_New_Username)
      print("Sucess!")

    elif Change_setting_anwser == "BOTH":
      print("Enter in your username!") 
      Users_New_Username = input(": ")
      print("Enter in your new password!")
      # Users_New_Password = input(": ")
      Users_New_Password = getpass.getpass(": ")
      with open("masterPassword.txt", "w") as Change_password_file:
        Change_password_file.write(Users_New_Password)
      with open("usersName.txt", "w") as Change_name_file:
        Change_name_file.write(Users_New_Username)
      print("Sucess!")



checkForFile1 = (os.path.exists("usersName.txt"))
checkForFile2 = (os.path.exists("masterPassword.txt"))
if checkForFile1 and checkForFile2 == True:
  pass
else:
  ToesManager.Inital_Setup()

with open("usersName.txt", "r") as readUsersName:
  nameOfUser = readUsersName.readline()
with open("masterPassword.txt", "r") as readMasterPassword:
  usersMasterPasswd = readMasterPassword.readline()

Password_Tries = 0
while Password_Tries < 3:

  print("Enter you Password")
  # User_Entered_Password = input(": ")
  User_Entered_Password = getpass.getpass(": ")
  Password_Tries += 1 


  if User_Entered_Password == usersMasterPasswd:
    while True:
      # ToesManager.tess()
      command = input("(type HELP, for commands): ").upper()
      if command == "NEW":
          ToesManager.Generate_Password()
      elif command == "CHECK":
          ToesManager.Check_Password()
      elif command == "ADD":
          ToesManager.Add_Password()
      elif command == "QUIT" or "EXIT":
          ToesManager.Quiting_Program()
      elif command == "HELP":
          ToesManager.Help()
      elif command == "CLEAR":
          ToesManager.Clear_Console()
      elif command == "CHANGE":
          ToesManager.Change_Settings()
      else:
          print("wrong command - type HELP for help")
  else:
    print("Wrong Password")
else:
    print("User Verification failed")
    sleep(2)
    quit()




