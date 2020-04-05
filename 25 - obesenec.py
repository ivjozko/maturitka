import re
import random

f = open('obesenec.txt','r').read()

slova = re.findall(r'[A-z]+',f)
slovo = random.choice(slova)
print('-'*len(slovo),'\nHadaj slovo')

zle = None
win = False
poc = 0
hadane_slovo = [('-') for i in range(len(slovo))]

while not win:
    zle = True
    inp = input()
    for i in range(len(slovo)):
        if str(inp) == str(slovo[i]):
            hadane_slovo[i] = inp
            zle = False

    if zle:
        poc += 1

    for pis in hadane_slovo:
        print(pis,end='')
    print(' ',poc,'zlych pokusov')

    if poc == 10:
        print('Neuhadol si slovo!')
        break
    if '-' not in hadane_slovo:
        print('Gratulujem uhadol si slovo!')
        break
