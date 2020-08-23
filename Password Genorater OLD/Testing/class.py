import random

class passwordapp:
    def __init__(self, software_name, username, password):
        self.software_name = software_name
        self.username = username
        self.password = password
    
    def display_password(self):
        print(f"Your Username and Password for {self.software_name} is {self.username} {self.password}")


one = ""
two = ""




test1 = input("Enter the web")
test2 = input("Enter the username")


lower = "abcdefghijklmnopqrstuvwxyz"
higher = "ABCDEFGHIFJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()+=/"

test = lower + higher + symbols
length = 10

Password = "".join(random.sample(test, length))


one = passwordapp(test1, test2, Password)



one.display_password

