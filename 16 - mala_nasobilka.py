import random

poc = 0
acko = []
bcko = []
vysledko = []
while poc < 10:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if a*b <= 100:
        vys = a*b
        poc += 1
        acko.append(a)
        bcko.append(b)
        vysledko.append(vys)


body = 0
i = 0
zmensovanie_i = 0
indexiky = []

for i in range(10):
    print(acko[i], '*', bcko[i], '=')
    vstup = int(input())
    if vstup is int(vysledko[i]):
        print('Spravne!')
        body += 1

        zmensovanie_i += 1

    else:
        print('Zle!')
        indexiky.append(i)

if len(indexiky) != 0:
    for i in indexiky:
        print(acko[i], '*', bcko[i], '=')
        vstup = int(input())
        if vstup is int(vysledko[i]):
            print("Na druhy pokus spravne!")
        else:
            print("Aj na druhy pokus zle!")

print("Ziskal si",body,"bodov!")






