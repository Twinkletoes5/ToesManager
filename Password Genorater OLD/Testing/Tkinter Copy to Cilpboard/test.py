from tkinter import *
import random

root = Tk()

root.geometry("1000x1000")
root.title("Password Keeper")


txt1 = Label(root, text = "How can I help you today?", font = ("Bold", 50))
txt1.grid(column = 0, row = 0)

Start_app = False

def NewWindow():
    window = Toplevel()
    window.geometry("500x500")
    window.title("New Password")
    Start_app = True


new_password_btn = Button(root, text = "NEW", font = ("Bold", 50), command = NewWindow)
new_password_btn.grid(column = 0, row = 1)

'''
def NewPassword():
    lower = "abcdefghijklmnopqrstuvwxyz"
    higher = "ABCDEFGHIFJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()+=/"

    test = lower + higher + symbols
    length = 16

    #Password = Label(window, text = "".join(random.sample(test, length))
    #Password.grid(column = 0, row = 1)
'''

if Start_app:
    password_txt = Label(window, text = "Here is you new Password: adgasdfgasdfasdf")
    password_txt.grid(column = 0, row = 0)


close_btn = Button(root, text = "Close", command = root.destroy)
close_btn.grid(column = 10, row = 10)


root.mainloop()

