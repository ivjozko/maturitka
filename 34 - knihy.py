import re
import math
f = open('knihy.txt','r').read()

nazvy = re.findall(r'[A-z ]+',f)
datumy = re.findall(r'[\d ]+',f)

nazvy = [(i)for i in nazvy if i != ' ']
datumy = [(i)for i in datumy if i != ' ']

upomienka = []
maxx = 0
najpozic = []
dlzka_pozicania = []
for i in range(len(datumy)):
    rozdel = datumy[i].split()
    dokopy = 0
    for j in range(math.floor(len(rozdel)/2)):
        j *= 2
        dokopy += (int(rozdel[j+1])//100 - int(rozdel[j])//100)
    dlzka_pozicania.append(dokopy)
    if len(datumy[i]) > maxx:
        maxx = len(datumy[i])
        najpozic = nazvy[i]
    if len(datumy[i])%2 == 0:
        upomienka.append(nazvy[i])
    else:
        pass
print('Upomienku treba poslat na knihy',upomienka)
print('Najviac sa poziciava kniha',najpozic)
zoradene = [x for _, x in sorted(zip(dlzka_pozicania,nazvy))]
print('Zoradene knihy podla pozicania: ',zoradene)
