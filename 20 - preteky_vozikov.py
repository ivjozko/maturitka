from tkinter import *
import random

root = Tk()

s = root.winfo_screenwidth()
h = root.winfo_screenheight()

c = Canvas(root,width = s, height = h)
c.place(x = -2,y = -2)

root.attributes("-fullscreen",True)

x=40
x1=40
y=40
def chod ():
    rychlosti = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    c.delete("all")
    global x
    global x1
    x += random.choice(rychlosti)
    x1 += random.choice(rychlosti)
    c.create_rectangle(x, y, x + 100, y + 50, fill='red')
    c.create_oval(x, y + 40, x + 40, y + 80, fill='black')
    c.create_oval(x + 60, y + 40, x + 100, y + 80, fill='black')

    c.create_rectangle(x1, y+200, x1 + 100, y + 250, fill='blue')
    c.create_oval(x1, y + 240, x1 + 40, y + 280, fill='black')
    c.create_oval(x1 + 60, y + 240, x1 + 100, y + 280, fill='black')

    if x1 > 1540 or x > 1540:
        root.after_cancel(vyhodnotenie())


    a = 1450
    b = 0
    while a < 1530:
        while b < 800:
            c.create_rectangle(a, b, a + 10, b + 10, fill='black')
            b += 20
        a += 10
        b -= 810
    root.after(20,chod)

def vyhodnotenie():
    if x > x1:
        lb = Label(root, text='vyhral cerveny', font=('Arial', 30))
        lb.place(x=400, y=300)
    if x < x1:
        lb = Label(root, text='vyhral modry', font=('Arial', 30))
        lb.place(x=400, y=300)

ex = Button(root, text = 'exit',command = root.destroy)
ex.place(x = 0,y = 0)

b1 = Button(root, text = 'chod',command = chod)
b1.place(x = 30,y = 0)


mainloop()