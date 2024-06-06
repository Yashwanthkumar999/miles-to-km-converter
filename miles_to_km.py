from tkinter import *

window = Tk()
window.title("Miles to Kilometers converter")
window.config(padx=50, pady=50)


def converter():
    miles = float(miles_input.get())
    KM = round(miles * 1.609)
    km_result.config(text=f"{KM}")


def clear():
    km_result.config(text="0")


miles_input = Entry()
miles_input.grid(column=2, row=2)

miles_label = Label(text="Miles")
miles_label.grid(row=2, column=3)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=3, column=1)

km_result = Label(text="0")
km_result.grid(row=3, column=2)

km = Label(text="Km")
km.grid(row=3, column=3)

calculate = Button(text="Calculate", command=converter)
calculate.grid(row=4, column=2)

clea_scr = Button(text="clear", command=clear)
clea_scr.grid(row=5,column=2)

window.mainloop()
