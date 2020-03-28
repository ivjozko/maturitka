import re
import statistics
import tkinter
subor = open("spokojnost.txt",'r').read()
spokojnost = re.findall(r'nie|ano',subor)
cas = re.findall(r'[0-9]+[:][0-9]+',subor)
print("Negativnych vyjadreni bolo",len(re.findall('nie',subor)),'.')
hodiny = re.findall(r'[^:]\d\d',subor)

zle_hod = []
for i in range(len(hodiny)):
    if spokojnost[i] == 'nie':
        zle_hod.append(hodiny[i])
print("Najnespokojnejsi ludia boli pocas",statistics.mode(zle_hod),"hodiny a bolo ich", len(statistics.mode(zle_hod)),".")

nespokojni = 0
for i in range(len(hodiny)):
    if hodiny[i] != hodiny[-1]:
        if hodiny[i] != hodiny[i + 1] and spokojnost[i] == 'ano':
            print("Nespokojnych ludi pocas", hodiny[i], "hodiny bolo 0.")
        if hodiny[i] == hodiny[i + 1] and spokojnost[i] == 'ano':
            pass
        if hodiny[i] != hodiny[i + 1] and spokojnost[i] == 'nie':
            nespokojni += 1
            print("Nespokojnych ludi pocas", hodiny[i], "hodiny bolo", nespokojni, ".")
            nespokojni = 0
        if hodiny[i] == hodiny[i + 1] and spokojnost[i] == 'nie':
            nespokojni += 1
    else:
        print("Nespokojnych ludi pocas", hodiny[i], "hodiny bolo 1.")


canvas = tkinter.Canvas(bg="white", height=520, width=480)
canvas.pack()

x = 10
cisla = ' '
poc = -1
pocitadlo = -1
for i in range(24):
    pocitadlo += 1
    if pocitadlo < 10:
        cisla = ' 0'
        cisla += str(pocitadlo)
    if pocitadlo >= 10:
        cisla = ' '
        cisla += str(pocitadlo)
    canvas.create_text(x,510,text = cisla, font = ('Arial',10))
    canvas.create_line(x-7,500,x+10,500,width = 2,fill='black')
    if cisla in hodiny:
        poc_nie = 0
        for i in range(int(hodiny.count(cisla))):
            poc += 1
            if spokojnost[poc] == 'nie':
                poc_nie += 1
                canvas.create_line(x+1, 500, x+1, 500 - 50 * poc_nie, width=15, fill='red')
    x += 20

pocet_debilov = 0
y = 500
for i in range(8):
    pocet_debilov += 1
    y -= 50
    canvas.create_text(10,y,text= pocet_debilov, font = ('Arial',10))
canvas.mainloop()
