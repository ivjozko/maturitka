import random
import re

cisla = input("Zadaj 6 cisel od 1 - 49: ")

ciselka = re.findall(r'\d+',cisla)
print(ciselka)

for i in ciselka:
    if int(i) > 49:
        print("Zadal si cislo vacsie ako 49!")
        break

vyherne_cisla = []
for i in range(6):
    x = random.randint(1,49)
    vyherne_cisla.append(x)
print(vyherne_cisla)

zhoduju_sa = []
for i in vyherne_cisla:
    for j in ciselka:
        if int(i) == int(j):
            zhoduju_sa.append(j)
print("Zhodne cisla :",zhoduju_sa)

subor = open("loteria.txt","r").read()
guys = re.findall(r'\d+',subor)

vsetci = []
for i in range(len(guys)//6):
    vsetci.append([])

poc = 0
poci = 0
for i in range(len(guys)):
    vsetci[poci].append(guys[i])
    poc += 1
    if poc == 6:
        poc = 0
        poci += 1

nic = 0
zhoda_1 = 0
zhoda_2 = 0
zhoda_3 = 0
zhoda_4 = 0
zhoda_5 = 0
zhoda_6 = 0
pocitadlo = 0
for typek in vsetci:
    for cislo in typek:
        if int(cislo) in vyherne_cisla:
            pocitadlo += 1
    if pocitadlo == 0:
        nic += 1
    if pocitadlo == 1:
        zhoda_1 += 1
    if pocitadlo == 2:
        zhoda_2 += 1
    if pocitadlo == 3:
        zhoda_3 += 1
    if pocitadlo == 4:
        zhoda_4 += 1
    if pocitadlo == 5:
        zhoda_5 += 1
    if pocitadlo == 6:
        zhoda_6 += 1
    pocitadlo = 0

print("Neuhadli cislo:",nic)
print("Uhadli jedno cislo:",zhoda_1)
print("Uhadli dve cisla:",zhoda_2)
print("Uhadli tri cisla:",zhoda_3)
print("Uhadli styri cisla:",zhoda_4)
print("Uhadli pät cisel:",zhoda_5)
print("Uhadli sest cisel:",zhoda_6)

