import os
import platform


def Clear_Console():
  User_Platform = platform.system()
  if User_Platform == "Darwin":
    os.system('clear')
  elif User_Platform == "Windows":
    os.system('clr')