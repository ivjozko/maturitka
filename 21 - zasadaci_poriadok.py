import re
import random
from tkinter import *
root = Tk()
v = root.winfo_screenheight()
s = root.winfo_screenwidth()
canvas = Canvas(root,height = v, width = s, bg = 'White')
canvas.place (x = -2, y = -2)
ex = Button(root, text = 'EXIT', bg = 'Gray', command = root.destroy)
ex.place(x = 0, y = 0)
root.attributes("-fullscreen",True)

subor = open('zasadaci_poriadok.txt','r').read()

ziaci = re.findall(r'[A-z]+',subor)

canvas.create_text(700,680, text = 'Pocet radov')
entry_rady = Entry(root)
canvas.create_window(700,700,window = entry_rady)
canvas.create_text(700,750, text = 'Pocet lavic v rade')
entry_lavice = Entry(root)
canvas.create_window(700,770,window = entry_lavice)

def vykresli ():
    canvas.create_rectangle(50,50,1500,600,fill = 'White')
    rady = int(entry_rady.get())
    lavice = int(entry_lavice.get())
    x = 0
    y = 0
    poc = 0
    if rady * lavice < int(len(ziaci)/2):
        canvas.create_text(750, 400, fill = 'Red', text = 'Mate malo lavic na usadenie studentov!', font = ('Arial', 50))
    else:
        for i in range(rady):
            y += 60
            for j in range(lavice):
                x += 110
                canvas.create_rectangle(x, y, x + 100, y + 50)
                try:
                    canvas.create_text(x + 50, y + 10, text=ziaci[poc], fill='Red')
                    canvas.create_text(x + 50, y + 30, text=ziaci[poc + 1], fill='Black')
                    poc += 2
                except IndexError:
                    pass
                if j == lavice - 1:
                    x = 0

potvrd = Button(root,text = 'Potvrd vstup', command = vykresli)
potvrd.place(x = 650, y = 800)
mainloop()