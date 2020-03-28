import re
subor = open("ucenie_sa_slovicok.txt",'r').read()
slovicka = re.findall(r'[A-z]+',subor)

co_chce = int(input("Pre skusanie anj zadaj 1 pre sjl 2!"))

body = 0
i = 0
zle_body = 0
vyradit = []
if co_chce == 1:
    while len(slovicka) != 0:
        for i in range(int(len(slovicka) / 2)):
            print("Zadaj preklad slova", slovicka[i*2])
            vstup = input()
            if vstup == slovicka[i*2 + 1]:
                vyradit.append(slovicka[i*2])
                vyradit.append(slovicka[i*2+1])
                print("Dobre!")
            else:
                zle_body += 1
                print("Zle!")

        for i in range(len(vyradit)):
            slovicka.remove(str(vyradit[i]))
        vyradit = []
print("Zlych pokusov si mal", zle_body)

if co_chce == 2:
    while len(slovicka) != 0:
        for i in range(int(len(slovicka) / 2)):
            print("Zadaj preklad slova", slovicka[i*2+1])
            vstup = input()
            if vstup == slovicka[i*2]:
                vyradit.append(slovicka[i*2])
                vyradit.append(slovicka[i*2+1])
                print("Dobre!")
            else:
                zle_body += 1
                print("Zle!")

        for i in range(len(vyradit)):
            slovicka.remove(str(vyradit[i]))
        vyradit = []
print("Zlych pokusov si mal", zle_body)