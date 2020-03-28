import re
import random

subor = open('obesenec.txt','r').read()
slova = re.findall(r'[A-z]+',subor)
print(slova)
slovo = random.choice(slova)
print(slovo)
hadane_slovo = ("-"*len(slovo))
print("Zahrame si hru obesenec. Postupne hadaj pismena: ",hadane_slovo)

for i in range(10):
    pismeno = input()
    if pismeno in slovo:
        hodnota = slovo.find(pismeno)
        hadane_slovo = list(hadane_slovo)
        hadane_slovo[hodnota] = pismeno
        print("super uhadol si pismeno, pokracuj", "".join(hadane_slovo))
        if "-" not in hadane_slovo:
            break
            print("Gratulujem uhadol si slovo.")
    else:
        print("zle, toto pismeno sa tam nenachadza", "".join(hadane_slovo))
if i == 9:
    print("Neuhadol si slovo.")
