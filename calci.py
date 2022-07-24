from tkinter import *
import tkinter.font as font

frame = Tk()  
frame.geometry("400x500")
frame.title("Calculator")
frame.iconbitmap("images/calsi.ico")
frame.configure(bg='cyan')
buttonfont = font.Font(family='Helvetica', weight='bold')
txtfont = font.Font(family='verdana', weight='bold' , size=15)
val = StringVar()
a = 60
b = 120
count = 1

v1 = 0.0
v2 = 0.0
v3 = 0.0
op = 0

def display(event):
    global op
    global v1
    global v2
    global v3
    but = (event.widget)
    st = but.cget('text')
    
#    print(st)`
    
    if(st=="Clr"):
        v1 = 0.0
        v2 = 0.0
        v3 = 0.0
        val.set('')
        return
    
    if(st=="Back"):
        val.set(val.get()[:len(ss)-1])
        return
        
    if(val.get()=="Infinity"):
        val.set('')
    
    if(not(st=='+' or st=='-' or st=='*' or st=='/' or st=='=')):
        ss = val.get()
        if(st=='.' and ss.find('.')==-1):
            val.set(val.get()+((but.cget('text'))))
        elif not st=='.':
            val.set(val.get()+((but.cget('text'))))

    if st=='+':
        v1 = float(val.get())
        val.set('')
        op = 1
        
    if st=='-':
        v1 = float(val.get())
        val.set('')
        op = 2
        
    if st=='*':
        v1 = float(val.get())
        val.set('')
        op = 3
        
    if st=='/':
        v1 = float(val.get())
        val.set('')
        op = 4

    if st=='=':
        v2 = float(val.get())
        if(op==1):
            v3 = v1 + v2
            val.set(str(v3))
            
        if(op==2):
            v3 = v1 - v2
            val.set(str(v3))

        if(op==3):
            v3 = v1 * v2
            val.set(str(v3))

        if(op==4):
            if(v2==0):
                val.set("Infinity")
            else:
                v3 = v1 / v2
                val.set(str(v3))
            
ls = ["1","2","3","4","5","6","7","8","9","0","+","-","*","/",".","=","Clr","Back"] 
butls = []

txt = Entry(frame , width=24 , font=txtfont , justify=RIGHT , textvariable=val)
txt.place(x=60,y=40,width=272,height=40)

for i in range(0,18):
    butls.append(Button(frame , text=str(ls[i]) , width="4" , height="1" , font=buttonfont))
    butls[i].place(x = a ,y = b)
    butls[i].bind("<Button-1>",display)
    if(count < 4):
        a = a + 70
        count = count + 1
    else:
        b = b + 60
        a = 60
        count = 1

frame.mainloop()
