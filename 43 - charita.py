import re
subor = open('charita.txt','r').read()
hodnoty = re.findall(r'[0-9]+',subor)

cisla = []
for i in hodnoty:
    cisla.append(int(i))

print("Pocet volani: ",len(hodnoty))
print("Vyzbierana suma: ", sum(cisla))
print("Najvacsia hodnota prispevku: ", max(cisla))