f = open('rys.txt', 'r').read()
import re, math

cisla = re.findall(r'\d+', f)
xka = []
yka = []
for i in range(len(cisla)):
    if i % 2 == 0:
        xka.append(cisla[i])
    else:
        yka.append(cisla[i])

xka = [int(i) for i in xka]
yka = [int(i) for i in yka]

print(xka, yka)

celkova = 0
vela = 0
for i in range(len(xka) - 1):
    a = math.sqrt(((yka[i] - xka[i]) ** 2) + ((yka[i+1] - xka[i+1]) ** 2))
    celkova += a
    if a > vela:
        vela = a
        den = i + 1
print("Najvacsia vzdialenost",round(vela,2), 'v den cislo:', den)
print("Celkova vzdialenost je",round(celkova,2))
