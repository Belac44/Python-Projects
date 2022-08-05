from tkinter import *
import math

window = Tk()
window.minsize(width=400, height=300)
window.title("Miles to Km Converter")
window.config(padx=100, pady=100)

inputs = Entry(width=10)
inputs.grid(column=3, row=1)

miles = Label(text="Miles")
miles.grid(column=4, row=1)

equal = Label(text="is equal to")
equal.grid(column=2, row=2)

converted = Label(text="")
converted.grid(column=3, row=2)

km = Label(text="Km")
km.grid(column=4, row=2)


def convert():
    converted['text'] = math.ceil(int(inputs.get()) * 1.6)


button = Button(text="calculate", command=convert)
button.grid(column=3, row=3)

window.mainloop()
