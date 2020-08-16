import random
import time
import string
import pyperclip


password_tries = 0 
while password_tries < 3:

    enter_password = input("Enter Password: ")
    right_password = "5eanisatCA"
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
                    writePasswordtoFile.write(f"{name_of_software}: \nUserName: {username}\nPassword: {Password}\n\n")
                    writePasswordtoFile.close()

            elif command == "ADD":
                add_appName = input("Enter the Website or App: ")
                add_userName = input("Enter the username for it: ")
                
                while True:
                    add_passWord = input("Enter the password for it: ")
                    add_passWord_Verify = input("Verify your password: " )

                    if add_passWord == add_passWord_Verify:
                        with open("Passwords.txt" , "a") as addPasswords:
                            addPasswords.write(f"{add_appName}: \nUserName: {add_userName}\nPassword: {add_passWord}\n\n")
                            addPasswords.close()

                        print("Sucess!")
                        break
                    
                    elif ask3 != ask4:
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
        print('You are not Sean You son of a bitch!!!')

else:
    print("Nah, get out man")
    time.sleep(2)
    quit()


