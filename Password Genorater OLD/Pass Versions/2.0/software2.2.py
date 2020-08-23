import random
import time


password_tries = 0 #also add a time out, so after some time it will have to reeneter the password for Verison 2.x

while password_tries < 3:

    enter_password = input("Enter Password: ") #add limited tries in the program. So the user only gets three try from entering the password (By adding an If statement?) No You dont add "if" you add while loop and change the condition
    right_password = "5eanisatCA"
    quit_password = "QUIT"
    password_tries = password_tries + 1

    if enter_password == right_password:

        while True:
            command = input("How can I help you today?: ").upper()
    
            if command == "NEW":
                name_of_software = input("Enter the web or app name: ")
                username = input("Enter your username: ")
                input_length = int(input("Enter the length: "))
                lower = "abcdefghijklmnopqrstuvwxyz"
                higher = "ABCDEFGHIFJKLMNOPQRSTUVWXYZ"
                symbols = "!@#$%^&*()+=/"
                numbers = "1234567890"

                test = lower + higher + symbols + numbers
                length = input_length

                Password = "".join(random.sample(test, length))

                print(Password)
                   

                
                print("Aight bet.")

                file_append = open("Passwords.txt", "a")
                file_append.write(f"\n {name_of_software} [{username}: {Password}]")
                file_append.close()

            elif command == "CHECK":
                file_read = open("Passwords.txt", "r")
                print(file_read.read())
                file_read.close()

            elif command == "QUIT":
                print("Closing...")
                time.sleep(3)
                quit()
                #sys.exit()


            else:
                print("Wrong thing mate")

    elif enter_password.upper() == quit_password:
        print("Closing...")
        time.sleep(3)
        break

    else:
        print('You are not Sean You son of a bitch!!!')
else:
    print("Nah, get out man")

time.sleep(3)

