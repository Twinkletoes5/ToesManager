#2.0 is going have more inputs
import random
from string import digits
from string import punctuation
from string import ascii_letters
import sys
import time

need_to_enter_password_again = time.time()+ 60 * 2

password_tries = 0 #also add a time out, so after some time it will have to reeneter the password for Verison 2.2

while password_tries < 3:

    enter_password = input("Enter Password: ") #add limited tries in the program. So the user only gets three try from entering the password (By adding an If statement?) No You dont add "if" you add while loop and change the condition
    right_password = "5eanisatCA"
    quit_password = "QUIT"
    password_tries = password_tries + 1

    if enter_password == right_password:

        while time.time() < need_to_enter_password_again:
            command = input("How can I help you today?: ").upper()
    
            if command == "NEW":
                name_of_software = input("Enter the web or app name: ")
                username = input("Enter your username: ")


                test = ascii_letters + digits + punctuation
                random_test = random.SystemRandom()
                password = "".join(random_test.choice(test) for x in range(16))

                print("Aight bet.")

                file_append = open("Passwords", "a")
                file_append.write(f"\n {name_of_software} ({username}: {password})")
                file_append.close()

            elif command == "CHECK":
                file_read = open("Passwords", "r")
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
        sleep(3)
        break

    else:
        print('You are not Sean You son of a bitch!!!')
else:
    print("Nah, get out man")

time.sleep(3)
