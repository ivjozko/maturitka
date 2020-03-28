from tkinter import *
root = Tk()
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()


root.attributes("-fullscreen",True)
a=21

def semafor():
    global a
    if a >11:
        canvas.create_rectangle(200, 200, 400, 700, fill='black')
        canvas.create_oval(250, 250, 350, 350, fill='red')
        canvas.create_oval(250, 400, 350, 500, fill='grey')
        canvas.create_oval(250, 550, 350, 650, fill='grey')
        canvas.create_text(300, 300, text=a-11)
        a -= 1

    elif a < 12 and a > 10:
        canvas.create_rectangle(200, 200, 400, 700, fill='black')
        canvas.create_oval(250, 250, 350, 350, fill='red')
        canvas.create_oval(250, 400, 350, 500, fill='orange')
        canvas.create_oval(250, 550, 350, 650, fill='grey')
        canvas.create_text(300, 300, text=a - 11)
        a -= 1


    elif a <= 10 and a != 0:
        canvas.create_rectangle(200, 200, 400, 700, fill='black')
        canvas.create_oval(250, 250, 350, 350, fill='grey')
        canvas.create_oval(250, 400, 350, 500, fill='grey')
        canvas.create_oval(250, 550, 350, 650, fill='green')
        canvas.create_text(300, 600, text=a)
        a-=1

    else:
        a = 20


    root.after(1000,semafor)


canvas = Canvas(root, width = sirka, height = vyska)
canvas.place(x=-2,y=-2)

ex=Button(root,text='exit',command=root.destroy)
ex.place(x = 0,y = 0)


semafor()

mainloop()