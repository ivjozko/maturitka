import re
subor = open('sr.txt','r').read()
suborik = open('sneh.txt','r').read()
hranice = re.findall(r'\d+',subor)
poloha_strediska = re.findall(r'\d+',suborik)

ix = []
iy = []
for i in range(len(hranice)):
    if i % 2 == 0:
        ix.append(hranice[i])
    if i % 2 != 0:
        iy.append(hranice[i])

polohax = []
polohay = []
poloha = []
for i in range(len(poloha_strediska)):
    if i % 3 != 0:
        poloha.append(poloha_strediska[i-1])
    else:
        pass
for i in range(len(poloha)):
    if i % 2 == 0:
        polohax.append(poloha[i])
    else:
        polohay.append(poloha[i])

info = re.findall(r'[A-z ]+ - [\d]+ cm - [A-z ]+',suborik)
print(info)


from tkinter import *
root = Tk()
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()

root.attributes("-fullscreen",True)

canvas = Canvas(root, width = sirka, height = vyska)
canvas.place(x=-2,y=-2)

for i in range(len(ix)):
    canvas.create_text(int(ix[i])+200,int(iy[i])+200,text = '.',font = ('Arial',10))

bod = None
poc = 0
lbl = Label(text = '')
lbl.place(x = 200,y = 25)
polohay = [int(i)for i in polohay]
polohax = [int(i)for i in polohax]
def click(event):
    try:
        global poc
        global bod
        canvas.delete(bod)
        canvas.create_rectangle(0, 0, 400, 50, fill='white')
        canvas.create_text(200, 20, text=info[poc])
        bod = canvas.create_oval(polohax[poc] + 200, polohay[poc] + 90, polohax[poc] + 210, polohay[poc] + 100,
                                 fill="red")
        poc += 1
    except IndexError:
        lbl.config(text = 'dalej uz nic neni')


ex=Button(root,text='exit',command=root.destroy)
ex.place(x = 0,y = 0)

root.bind("<Button-1>",click)

mainloop()