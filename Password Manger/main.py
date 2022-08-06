from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_credentials():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

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
generate = Button(text="Generate Password")
generate.grid(column=2, row=3)
add = Button(text="add", width=45, command=save_credentials)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()

