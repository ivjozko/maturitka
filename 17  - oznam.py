import re
veta = "Cez vikend je planovana odstavka severnej casti linky"

kusky = re.findall(r'[A-z]+',veta)
vieta = re.sub(r' ','',veta)

print(vieta)
print(kusky)

striedacka = []
k = 0
for i in kusky:
    if k%2 == 0:
        print(i.upper())
        striedacka.append(i.upper())
        k += 1
    else:
        print(i.lower())
        striedacka.append(i.lower())
        k += 1

print(striedacka)
print("Veta je z",len(striedacka),"slov")

stringac = ''
j = 0
for i in striedacka:
    if j%2 == 0:
        stringac += str(i.upper())
        stringac += ' '
        j += 1

    else:
        stringac += str(i.upper())
        stringac += ' '
        j += 1

print(stringac)
