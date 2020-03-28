from tkinter import *
import random
root = Tk()
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()



polohy=[50,100,150,200]
kabel = random.choice(polohy)
root.attributes("-fullscreen",True)
s = 1000
time = 5
def tick():
    canvas.delete(ALL)
    canvas.create_line(100, 50, 200, 50, width=20, fill='green')
    canvas.create_line(100, 100, 200, 100, width=20, fill='blue')
    canvas.create_line(100, 150, 200, 150, width=20, fill='red')
    canvas.create_line(100, 200, 200, 200, width=20, fill='yellow')
    canvas.create_line(100,kabel,200,kabel)
    canvas.create_oval(500,400,600,500,fill='black')
    global time
    global s
    time -= 1
    cas.config(text=time)
    if time == 0:
        lbl.config(text='bomba vybuchla')
        canvas.create_oval(100,100,1100,800,fill='yellow')
        bum = Label(root,text='BOooooooOM',font=60,bg = 'yellow')
        bum.place(x=600,y=400)
    else:
        root.after(s, tick)
root.after(1, tick)

def strih(event):
    global kabel
    global s
    a = event.x
    b = event.y
    if b > kabel-10 and b < kabel+10:
        lbl.config(text='zneskodnil si bombu')
        s = 100000000
    else:
        lbl.config(text='bomba vybuchla')
        canvas.create_oval(100, 100, 1100, 800, fill='yellow')
        bum = Label(root, text='BOooooooOM', font=60, bg='yellow')
        bum.place(x=600, y=400)
        s = 10000000






canvas = Canvas(root, width = sirka, height = vyska)
canvas.place(x=-2,y=-2)

ex=Button(root,text='exit',command=root.destroy)
ex.place(x = 0,y = 0)

lbl = Label(root,text='bezi ti cas musis prestrihnut kabel',font=30)
lbl.place(x=300,y=50)
cas = Label(root,text='60',font=30)
cas.place(x=300,y=150)
root.bind('<Button-1>',strih)


mainloop()