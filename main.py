import random
import time
import string
import pyperclip


password_tries = 0 
while password_tries < 3:

    enter_password = input("Enter Password: ")
    right_password = "5eanisatCA"
    quit_password = "QUIT"
    password_tries = password_tries + 1

    if enter_password == right_password:

        while True:
            command = input("How can I help you today?: ").upper()
    
            if command == "NEW":
                name_of_software = input("Enter the web or app name: ")
                username = input("Enter your username: ")

                try:
                    input_length = int(input("Enter the length: ")) #Use Try and Execpt, because it would break the program if user didn't use the right one 
                except ValueError:
                    print("Wrong Value")
                    continue


                speical_Letters = "!@#$%^&*_+=-~`<>/?()"
                new_password = string.ascii_uppercase + string.ascii_lowercase + string.digits + speical_Letters

                length = input_length

                Password = "".join(random.sample(new_password, length))

                print(Password)

                askIfNeedtoCopy = input("Do you want it to be copy to the clipboard? (Y/N): ").upper()
                if askIfNeedtoCopy == "Y":
                    pyperclip.copy(Password)
                else:
                    print("Alright then.")

                   
                print("Aight bet.")

                file_append = open("Passwords.txt", "a")
                file_append.write(f"\n{name_of_software}: [{username} - {Password}]")
                file_append.close()

            elif command == "ADD":
                ask1 = input("Enter the Website or App: ")
                ask2 = input("Enter the username for it: ")
                
                while True:
                    ask3 = input("Enter the password for it: ")
                    ask4 = input("Verify your password: " )

                    if ask3 == ask4:
                        with open("Passwords.txt" , "a") as addPasswords:
                            addPasswords.write(f"\n{ask1} : [{ask2} - {ask3}]")
                            addPasswords.close()

                        print("Sucess!")
                        break
                    
                    elif ask3 != ask4:
                        print("Try again.")
                        continue

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
