# Standard Library
import random
import string
import tkinter

# Third-Party Libraries
import pyperclip
from tkmacosx import Button

# Set up initial variables
password = ""
potential_char = ""

# Creates the string with potential characters in password
def generate_char():
    potential_char = ""
    if upper_var.get():
        potential_char += string.ascii_uppercase
    if lower_var.get():
        potential_char += string.ascii_lowercase
    if num_var.get():
        potential_char += string.digits
    if symbols_var.get():
        potential_char += string.punctuation
    return potential_char

# Checks for valid requirements, and generates random password
def generate():
    global password
    length = length_entry.get()
    # Make sure the entered length is a whole number within restriction
    try:
        length = int(length)
        if 8 <= length <= 32:
            
            # Checks for at least one checked checkbox
            checkboxes = [upper_var.get(), lower_var.get(), num_var.get(), symbols_var.get()]
            if any(b is True for b in checkboxes):
                password = ""
                potential_char = generate_char()
                for _ in range(length):
                    rand = random.randint(0,len(potential_char) - 1)
                    password += potential_char[rand]
                message_label.config(text=("Your generated password is " + password), fg = "green")
            else:
                message_label.config(text="Select at least one checkbox", fg="red")
        else:
            message_label.config(text="Enter integers within length restriction", fg="red")
    except ValueError:
        message_label.config(text="Enter valid integers", fg="red")

# Copies current password to clipboard
def copy():
    global password
    pyperclip.copy(password)
    message_label.config(text="Password has been copied to clipboard", fg = "lightblue")

# Window
window = tkinter.Tk()
window.title("Random Password Generator")
window.geometry("600x320")

title = tkinter.Label(window, text="Random Password Generator", font=("Times", 40))

password_length_frame = tkinter.Frame(window, width=300, height=100)
length_label = tkinter.Label(password_length_frame, text="Enter Password Length (8 to 32):", font=("Times", 20))
length_entry = tkinter.Entry(password_length_frame, width=5, bg="lightgray", fg="black")

# Check Buttons + Frame
check_btn_frame = tkinter.Frame(window, width=300, height=100)

upper_var = tkinter.BooleanVar()
lower_var = tkinter.BooleanVar()
num_var = tkinter.BooleanVar()
symbols_var = tkinter.BooleanVar()

upper_check_button = tkinter.Checkbutton(check_btn_frame , text="Include Uppercase", variable=upper_var)
lower_check_button = tkinter.Checkbutton(check_btn_frame , text="Include Lowercase", variable=lower_var)
num_check_button= tkinter.Checkbutton(check_btn_frame , text="Include Numbers", variable=num_var)
symbols_check_button = tkinter.Checkbutton(check_btn_frame , text="Include Symbols", variable=symbols_var)

# Generate and Copy Buttons
generate_btn = Button(window, text = "Generate", font = ("Times", 20), bg= "lightblue", fg = "black", 
                      activeforeground = "black", activebackground = "blue", command=generate)

copy_btn = Button(window, text = "Copy to Clipboard", font = ("Times", 20), bg= "lightblue", fg = "black", 
                  activeforeground = "black", activebackground = "blue", command=copy)

# Message to User Label
message_label = tkinter.Label(window, text="", font=("Times", 17), fg="red")

# Packing
upper_check_button.pack(side=tkinter.LEFT)
lower_check_button.pack(side=tkinter.LEFT)
num_check_button.pack(side=tkinter.LEFT)
symbols_check_button.pack(side=tkinter.LEFT)

length_label.pack(side=tkinter.LEFT)
length_entry.pack(side=tkinter.LEFT)

title.pack(pady=10)

password_length_frame.pack()
check_btn_frame.pack(pady=20)

generate_btn.pack(pady=5)
copy_btn.pack(pady=5)
message_label.pack(pady=15)

window.mainloop()