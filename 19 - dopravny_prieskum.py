import re

subor = open('dopravny_prieskum.txt','r').read()
nastup_vystup = re.findall(r'\d+',subor)
stanice  = re.findall(r'[A-z]+[ ]+[A-z]+|[A-z]+',subor)

nastup = []
vystup = []

for i in range(len(nastup_vystup)):
    if i % 2 == 0:
        nastup.append(nastup_vystup[i])
    else:
        vystup.append(nastup_vystup[i])

celkovo = 0
max = 0
treba_automat = []
treba_znamenie = []
for i in range(len(stanice)):
    celkovo = celkovo + int(nastup[i]) - int(vystup[i])
    print(stanice[i], celkovo)
    if celkovo > max:
        max = celkovo
    if int(nastup[i]) >= 10:
        treba_automat.append(stanice[i])
    if int(vystup[i]) <= 3:
        treba_znamenie.append(stanice[i])

if max >= 70:
    print("Odporucame dlhu elektricku!")
if max < 70 and max >= 30:
    print("Odporucame standardnu elektricku!")
if max < 30:
    print("Odporucame kratku elektricku!")

print("Automat treba na tychto staniciach!", treba_automat)
print("Na znamenie treba zmenit tieto stanice!", treba_znamenie)