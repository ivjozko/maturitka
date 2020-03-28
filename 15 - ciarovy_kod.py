from tkinter import *
import re
import random
root = Tk()
subor = open("ciarovy_kod.txt","r").read()

kody = re.findall(r'\d',subor)



def ciara(event):
    canvas = Canvas(root, bg="white", height=150, width=480)
    canvas.pack()

    x = 10
    y = 20
    poc = 0
    dlzka = 80
    x_c = 17
    for i in range(len(kody)):
        if poc == 1:
            dlzka = 60
        if poc == 7:
            dlzka = 80
        ciselko = random.randint(0,9)
        canvas.create_line(x, y, x, y + dlzka, width=ciselko)
        canvas.create_text(x_c, 90, font=('Arial', 10), text=ciselko)
        x += 10
        poc += 1
        x_c += 7.5
        if poc == 8:
            x_c += 35
            x += 15
            poc = 0
    root.mainloop()

root.bind('<space>',ciara)

root.mainloop()