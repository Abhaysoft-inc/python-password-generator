# Changing The Banner Doesn't makes you Programmer

#               Author : Abhay Vishwakarma
#         Special Thanks to geeksforgeeks.org


import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

# Function of Calculation Password

def low():
    entry.delete(0, END)

    # Get the length of the password
    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*() "
    password = ""

    # If Strength selected is low

    if var.get() == 1 :
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    # if strenght is selected as medium

    elif var.get() == 0 :
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    # if strength is selected as medium
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password

    else:
        print("Please Choose an option")    

# function for generating password 
def generate():
    password1 = low()
    entry.insert(10, password1)


# function for copying password
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

# Main Function
# creating GUI

root = Tk()
var = IntVar()
var1 = IntVar()

# Title of GUI

root.title("Python Password Generator")

# Create label and entry to show -
# Password Generated

Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# Create label of length of the password 

c_label = Label(root, text="Length of the password")
c_label.grid(row=1)

# Create Copy Button

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

# Radio Buttons

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_medium = Radiobutton(root, text="Medium", variable=var, value=0)
radio_medium.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')

combo = Combobox(root, textvariable=var1)

# Combo box for length of your password

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1)

root.mainloop()