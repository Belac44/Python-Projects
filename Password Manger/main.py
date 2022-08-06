from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
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
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_credentials():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web) < 1 or len(password) < 1 or len(email) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered\nEmail:{email}\nPassword:{password}\nIs iot ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                text = f"{web} | {email} | {password}"
                file.write(f"{text}\n")
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
web_entry = Entry(width=54)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "calebbosire44@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

#Buttons
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)
add = Button(text="add", width=45, command=save_credentials)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()

