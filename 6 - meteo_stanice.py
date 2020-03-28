import re
meteo = open("meteo_stanice.txt","r").read()

teploty = re.findall(r'[^0-9][+-][0-9]+[.][0-9]+',meteo)
print(teploty)

stanice = re.findall(r'[M][0-9]+',meteo)

print("Pocet merani = ",len(teploty))

najvissa = 0
string = ''
for hodnota in teploty:
    string = ''
    for pismeno in hodnota:
        if pismeno == '-':
            break
        if pismeno == '+':
            pass
        else:
            string += pismeno

    if string == ' ':
        pass
    else:
        x = float(string)
        if x > najvissa:
            najvissa = x

s_plus = ' +'
s_plus += str(najvissa)

print('Najvissia teplota', s_plus,'bola namerana na stanici s kodom', stanice[teploty.index(s_plus)],'.')

delitel = 0
scitanec = 0
for i in range(len(teploty)):
    delitel += 1
    scitanec += float(teploty[i])
priemer = scitanec/delitel
print("Preimerna teplota na vsetkych staniciach je",round(priemer,1),'.')
