import re

subor = open('skok_do_dialky.txt','r').read()
krajiny = re.findall(r'[A-Z][A-Z][A-Z]',subor)
skoky = re.findall(r'[0-9]+',subor)
mena = re.findall(r'[A-Z][a-z]+',subor)
print(krajiny)

for i in range(3):
    print("Krajina", krajiny[i],"ma",str(krajiny).count(krajiny[i]),"sutaziacich")

poc = 0
dokopy = 0
max = 0
vsetky = []
for i in skoky:
    poc += 1
    dokopy += int(i)
    if poc == 5:
        vsetky.append(dokopy)
        if dokopy > max:
            max = dokopy
        dokopy = 0
        poc = 0


print("Vyhral sutaziaci",mena[(str(vsetky).find(str(max))//6)],"s dlzkou skoku",max)