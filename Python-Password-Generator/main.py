import random
import pyperclip
from tkinter import *
from tkiner.ttk import *

# Function of Calculation Password

def low():
    entry.delete(0, END)

    # Get the length of the password
    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper