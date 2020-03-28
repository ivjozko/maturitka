st = '(a+b)-(((((())))a-b)*2)'
import re
from tkinter import *

zatvorky = re.findall(r'[()]', st)
ln = int(len(zatvorky))

parvae = re.findall(r'[(]', st)
lave = re.findall(r'[)]', st)

if ln % 2 == 0 or ln == 1:
    if len(parvae) == len(lave):
        for i in range(int(ln / 2)):
            if zatvorky[i] == '(':
                if zatvorky[i] == zatvorky[-(i + 1)]:
                    break
                else:
                    if zatvorky[i] == ')':
                        break
            else:
                break
else:
    print('zly pocet')

farby = ['blue', 'red', 'yellow', 'green', 'grey', 'pink']

root = Tk()
countre = 0
ct = 0
for i in st:
    if i == '(' or i == ')':
        if i == '(':
            l = Label(root, text=i, fg=farby[countre])
            l.place(x=ct, y=0)
            countre += 1
        elif i == ')':
            countre -= 1
            l = Label(root, text=i, fg=farby[countre])
            l.place(x=ct, y=0)


    else:
        l = Label(root, text=i, fg='black')
        l.place(x=ct, y=0)

    ct += 10

mainloop()