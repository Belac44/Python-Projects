from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    try:
        with open("data.json", "r") as data:
            data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="No file Saved",message="No Passwords saved yet")
    else:
        search_web = web_entry.get()
        if len(search_web) == 0:
            messagebox.showinfo(title="No Web Address", message="No Data File found")
        else:
            try:
                search_result = data[search_web]
            except KeyError:
                messagebox.showinfo(title="No Password", message="No details for the website exists")
            else:
                messagebox.showinfo(title="Password", message=f"Password Found\n\nEmail:{search_result['Email']}\n\nPassword:{search_result['Password']}\n")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_credentials():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        web:{
            "Email": email,
            "Password": password
        }
    }

    if len(web) < 1 or len(password) < 1 or len(email) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
             with open("data.json", "r") as data:
                data = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
emails = Label(text="Email/Username:")
emails.grid(column=0, row=2)
passwords = Label(text="Password:")
passwords.grid(column=0, row=3)

#Entries
web_entry = Entry(width=36)
web_entry.grid(column=1, row=1)
web_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "calebbosire44@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

#Buttons
search = Button(text="Search", width=16, bg="blue", command=search_password)
search.grid(column=2, row=1)
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)
add = Button(text="add", width=45, command=save_credentials)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()

