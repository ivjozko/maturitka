kluc = [4,6,2,4,9,5,3,2,1,2,6,5,4,9,5,4,2,3,6,4,2]
veta = str(input("Zadaj vetu s malymi pismenami: "))

sifra = ""
poc = 0
for pismeno in veta:
    if pismeno != " ":
        if ord(pismeno) + kluc[poc] > 122:
            x = ord(pismeno) + kluc[poc] - 26
            y = chr(x)
            sifra += y
        else:
            x = ord(pismeno) + kluc[poc]
            y = chr(x)
            sifra += y
    else:
        sifra += " "
    poc += 1
    if poc > len(kluc):
        poc = 0

print(sifra)