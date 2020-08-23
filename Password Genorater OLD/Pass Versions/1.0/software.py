import random
from string import digits
from string import punctuation
from string import ascii_letters
import sys
from time import *

def software():
    while True:

        enter_password = input("Enter Password: ")
        right_password = "5eanisatCA"
        quit_password = "QUIT"

        if enter_password == right_password:

            while True:
                command = input("How can I help you today?: ").upper()

                if command == "NEW":
                    name_of_software = input("Enter the web or app name: ")

                    test = ascii_letters + digits + punctuation
                    random_test = random.SystemRandom()
                    password = "".join(random_test.choice(test) for x in range(16))

                    print("This is your password for " + name_of_software + ": " + password)

                    file_append = open("Passwords", "a")
                    file_append.write("\n" + name_of_software + ": " + password)
                    file_append.close()

                elif command == "CHECK":
                    file_read = open("Passwords", "r")
                    print(file_read.read())
                    file_read.close()

                elif command == "QUIT":
                    print("Closing...")
                    sleep(3)
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


software()