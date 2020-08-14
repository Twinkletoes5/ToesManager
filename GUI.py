import random
import time 
import string
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Managing Toes Eh?")

correctPassword = "5eanisatCA"

def verifyIfPasswordisCorrect():
    print("Button working")

    if  == correctPassword:
        print("Correct Password")
        Label(root, text="Nicely Done!").pack()
    else:
        print("It didn't work")



enterPassword=""
enterPasswordLabel = Label(root, text="Enter your password").pack()
enterPassword = Entry(root, textvariable=enterPassword).pack()
submitBtn = Button(root, text="ENTER", command=verifyIfPasswordisCorrect).pack()


root.mainloop()

