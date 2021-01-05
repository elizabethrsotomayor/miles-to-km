from tkinter import *


def miles_to_km():
    miles = float(user_input.get())
    converted_miles = round(miles * 1.609)
    km_value.config(text=f"{converted_miles}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

user_input = Entry(width=10)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_value = Label(text="0")
km_value.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
