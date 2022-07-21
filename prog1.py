from tkinter import *

frame = Tk()
frame.geometry("400x150")
frame.title("Temperature Program")

ev1 = DoubleVar()
ev2 = DoubleVar()
ev3 = DoubleVar()

e1 = Entry (frame, textvariable = ev1)
e2 = Entry (frame, textvariable = ev2)
e3 = Entry (frame, textvariable = ev3)

l1 = Label (frame, text = "Enter Temperature")


def fahrenheit_show():
    ev2.set((ev1.get() * 9/5) + 32)
    ev3.set(ev1.get())
def celcius_setup():
    ev3.set(((ev1.get()-32)*5)/9)
    ev2.set(ev1.get())
btn1 = Button (frame, text = "Fahrenheit", command = fahrenheit_show)
btn2 = Button (frame, text = "Celcius", command = celcius_setup)
l1.place(x=10, y = 10)
e1.place (x = 120, y = 10)
btn1.place (x = 10, y = 50)
btn2.place (x = 10, y = 90)
e2.place (x = 120, y = 50)
e3.place (x = 120, y = 90)

frame.mainloop()
