import re
subor = open('jedla.txt','r').read()

jedla = re.findall(r'[a-z]',subor)
print("Pocet jedal na dalsi den je",len(jedla))

ziaci = re.findall(r'[0-9]+',subor)

z = 0
c = 0
m = 0
h = 0
for i in jedla:
    if i == 'z':
        z += 1
    if i == 'c':
       c += 1
    if i == 'm':
       m += 1
    if i == 'h':
       h += 1
print("Zelena",z)
print("Cervena",c)
print("Modra",m)
print("Hneda",h)

zoradene_jedla = ['z','c','m','h']
pocet = []
pocet.append(z)
pocet.append(c)
pocet.append(m)
pocet.append(h)

for i in range(4):
    if pocet[i] < 20:
        if zoradene_jedla[i] == 'z':
          print("Zelenych jedal je pod 20.")
        if zoradene_jedla == 'c':
          print("Cervenych jedal je pod 20.")
        if zoradene_jedla[i] == 'm':
          print("Modrych jedal je pod 20.")
        if zoradene_jedla == 'h':
          print("Hnedych jedal je pod 20.")
        print("Treba to ohlasit tymto studentom!")
        for j in range(len(jedla)):
            if jedla[j] == zoradene_jedla[i]:
                print(ziaci[j])


