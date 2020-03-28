from tkinter import *
import random
root = Tk()
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()
s= sirka/10
array = [s,s*2,s*3,s*4,s*5,s*6,s*7,s*8,s*9]
x = random.choice(array)

root.attributes("-fullscreen",True)



canvas = Canvas(root, width = sirka, height = vyska)
canvas.place(x=-2,y=-2)

ex=Button(root,text='exit',command=root.destroy)
ex.place(x = 0,y = 0)

canvas.create_rectangle(x,500,x+20,510,fill = 'green')


for i in range (9):
    y = s*(i+1)
    canvas.create_oval(y-30,480,y+50,530,fill = 'blue')

def ukaz(event):
    global x,y
    a = event.x
    b = event.y
    if a < x-45:
        lb.config(text='doprava')
    elif a > x+50:
        lb.config(text='dolava')
    elif a >= x-50 and a<= x+50:
        lb.config(text='nasiel si to')


lb = Label (root,text='nic',font=30)
lb.place(x=400, y=100)
root.bind('<Button-1>',ukaz)

mainloop()

