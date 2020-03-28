import re
subor = open("mena_zamestnancov.txt","r").read()
file = open("mena_zamestnancov2.txt","a")

mena = re.findall(r'[A-z]+[ ][A-z]+|[A-z]+',subor)

print("V subore je",int(len(mena)/2),"mien.")

vsetky = []
for i in range(int(len(mena)/2)):
    menecko = ''
    menecko = menecko + mena[i] + ' ' + mena[i+int(len(mena)/2)]
    menecko += '\n'
    vsetky.append(menecko)
    file.write(menecko)

najdlhsie_meno = ''
najdlhsie_priezvisko = ''
for i in range(int(len(mena)/2)):
    meno = mena[i]
    priezvisko = mena[i+int(len(mena)/2)]
    if len(meno) > len(najdlhsie_meno):
        najdlhsie_meno = meno
    if len(priezvisko) > len(najdlhsie_priezvisko):
        najdlhsie_priezvisko = priezvisko

print("Najdlhsie meno je", najdlhsie_meno,".")
print("Najdlhsie priezvisko je", najdlhsie_priezvisko,".")