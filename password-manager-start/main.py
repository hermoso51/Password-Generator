import tkinter
from tkinter import *
from tkinter import messagebox
import random

white = "#FFFFFF"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    complete_pass = password_letters + password_symbols + password_numbers
    random.shuffle(complete_pass)

    password = "".join(complete_pass)
    entry3.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    site = entry1.get()
    email = entry2.get()
    pass_word = entry3.get()

    if site and email and pass_word:
        with open("My_passwords.txt", "a") as file:
            file.write(f"{site} | {email} | {pass_word}\n")
            messagebox.showinfo(title="congrats", message="Password Saved!")
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
    else:
        messagebox.showwarning(title="Warning", message="Please fill in all fields!")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

Website = Label(text="Website:")
Website.grid(row=1, column=0)

entry1 = tkinter.Entry(width=47)
entry1.grid(column=1, row=1, columnspan=2)
entry1.focus()

Email_Username = Label(text="Email/Username:")
Email_Username.grid(row=2, column=0)

entry2 = tkinter.Entry(width=47)
entry2.grid(column=1, row=2, columnspan=2)
entry2.insert(0, "joshuahermoso08@gmail.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

entry3 = tkinter.Entry(width=29)
entry3.grid(column=1, row=3)


generate_pass = Button(text="Generate Password", width=14, command=password_generator)
generate_pass.grid(column=2, row=3)


add_btn = Button(text="Add", width=36, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()