import re
subor = open('zastavba_na_ulici.txt','r').read()
cisla = re.findall(r'\d+',subor)
pouzitelne_cisla = []
for i in cisla:
    pouzitelne_cisla.append(int(i))

vysky = []
sirky = []

for i in range(len(pouzitelne_cisla)):
    if i%2 == 0:
        sirky.append(pouzitelne_cisla[i])
    else:
        vysky.append(pouzitelne_cisla[i])
print(vysky)
print(sirky)
from tkinter import *
root = Tk()

v = root.winfo_screenheight()
s = root.winfo_screenwidth()

canvas = Canvas(root, height = v , width = s,bg = 'white')
canvas.place(x= -2,y = -2)

ex = Button(root,text = 'E X I T',bg = 'gray',command = root.destroy)
ex.place(x=0,y=0)

root.attributes("-fullscreen",True)

entry = Entry(root)
canvas.create_window(200, 350, window=entry)

def budovy ():
    prevysenie = int(entry.get())
    radius = sirky[0]
    start = 540
    for j in range(len(sirky)):
        if vysky[j] == 0:
            canvas.create_line(start + radius, 700 - vysky[j], start + radius + sirky[j], 700, fill='Green', width=2)
        else:
            canvas.create_rectangle(start + radius, 700 - vysky[j], start + radius + sirky[j], 700, fill='Grey')
        if j == 0:
            pass
        elif vysky[j] > vysky[j - 1]:
            if vysky[j - 1] == 0:
                pass
            elif vysky[j] - vysky[j - 1] > prevysenie:
                canvas.create_line(start + radius, 700 - vysky[j - 1], start + radius, 700 - vysky[j], fill='Red',
                                   width=2)
        if j == int(len(vysky) - 1):
            break
        elif vysky[j] > vysky[j + 1]:
            if vysky[j + 1] == 0:
                pass
            elif vysky[j] - vysky[j + 1] > prevysenie:
                canvas.create_line(start + radius + sirky[j], 700 - vysky[j + 1], start + radius + sirky[j],
                                   700 - vysky[j], fill='Red', width=2)
        radius += sirky[j]

button1 = Button(root,text='Max prevysenie', command=budovy)
button1.place(x = 200,y =  380)

mainloop()