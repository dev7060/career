from tkinter import *

frame = Tk()
frame.geometry("800x400")
frame.title("Numbers Swap")

ev1 = IntVar()
ev2 = IntVar()
ev3 = IntVar()

l1 = Label(frame, text = "Number 1")
l2 = Label(frame, text = "Number 2")
e1 = Entry(frame, textvariable=ev1)
e2 = Entry(frame, textvariable=ev2)
def swap_fun():
    ev3.set(ev1.get())
    ev1.set(ev2.get())
    ev2.set(ev3.get())
    
btn = Button(frame, text = "Swap", command = swap_fun)

l1.place (x = 10, y=10)
l2.place (x = 150, y=10)
e1.place (x = 10, y=40)
e2.place (x = 150, y=40)


btn.place(x=120, y = 80)

frame.mainloop()
