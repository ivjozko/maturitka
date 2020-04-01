veta = 'Juchu konecne som zmaturoval. a nazdar bazar ty nula'
dlzka = len(veta)
arr = []
for i in range(1,17):
    arr.append(i*i)
    if i != 16:
        arr.append(i*(i+1))

rozdiel = 1000
for i in range(len(arr)):
    if dlzka-arr[i] < rozdiel and dlzka-arr[i] >= 0:
        rozdiel = dlzka-arr[i]
        ind = i+1

for i in range(1,17):
    sker = (i*i)
    if (i*i) == arr[ind]:
        a = i
        b = i
    if (i*(i+1)) == arr[ind]:
        a = i
        b = i+1

veticka = [[] for _ in range(a)]
poc = 0
for i in range(a):
    for j in range(b):
        veticka[i].append(veta[poc])
        poc += 1
        if poc == len(veta):
            break
dlzka = len(veta)
while a*b-dlzka != 0:
    veticka[-1].append(' ')
    dlzka+=1

for riadok in veticka:
    for prvok in riadok:
            print('', prvok, end='  ')
    print()

print('_____________________________________')

import random
arrrr = [i for i in range(b)]
for iad in range(len(veticka)//2):
    c = random.choice(arrrr)
    d = random.choice(arrrr)
    for i in range(len(veticka)):
        veticka[i][c],veticka[i][d] = veticka[i][d],veticka[i][c]
for riadok in veticka:
    for prvok in riadok:
            print('', prvok, end='  ')
    print()