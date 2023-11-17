import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

# Create the window
wn = Tk()
wn.title("Computer-Arranger")
wn.geometry("700x500")
#wn.wm_iconbitmap('bookmark.ico')

# Introduction text
intro_txt1 = Label(wn, text="Welcome to Computer-Arranger!")
intro_txt2 = Label(wn, text="This program will arrange your messy computer!")
intro_txt1.grid(row=0, column=0)
intro_txt2.grid(row=1, column=0)

def path():
    # Print the current working directory
    print(os.getcwd())

def choice_file():
    global folder
    label = Label(wn, text="Choose the folder you want to arrange:", bg='LightSteelBlue3', bd=1, relief=RAISED, width=30)
    label.grid(row=2, column=0)

    folder = ttk.Combobox(wn, values=path(), width=15)
    folder.grid(row=2, column=1)

def check_arrange():
    global choose
    label = Label(wn, text="\n\n\n\n\n")
    label.grid(row=3, column=0)
    choices = ["arrange by name", "arrange by ending", "arrange by size"]
    choose = ttk.Combobox(wn, values=choices, width=20)
    choose.grid(row=3, column=0)

def add_arrange():
    global letter, text
    space = Label(wn, text="         ")
    choice = choose.get()
    wn.counter += 1
    if choice == "arrange by name":
        # Print the selected choice
        print(f"You chose: {choice}")

        # Get the letters from the user
        lab = Label(wn, text="Put all the files contains the letters:", bg='LightSteelBlue2', bd=1, relief=RAISED, width=30)
        lab.grid(row=wn.counter + 4, column=0)

        letter = Entry(wn)
        letter.grid(row=wn.counter + 4, column=1)

        # Get the text from the user
        lab2 = Label(wn, text="in the fold:", bg='LightSteelBlue2', bd=1, relief=RAISED, width=10)
        lab2.grid(row=wn.counter + 4, column=3)

        text = Entry(wn)
        text.grid(row=wn.counter + 4, column=4)

        # Create a new folder
        new_folder = os.path.join(os.getcwd(), f"{letter}{text}")
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        # Move the files to the new folder
        for file in os.listdir(os.getcwd()):
            if file.startswith(letter):
                file_path = os.path.join(os.getcwd(), file)
                shutil.move(file_path, new_folder)

def new_button():
    add = Button(wn, text="New", bd="5", command=add_arrange, state="normal")
    add.grid(row=3, column=1)

    

wn.mainloop()