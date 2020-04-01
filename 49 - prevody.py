import re
s = "101001 2 42 8 FA 16 FF 16 1010001 2 50 8 "
hodnoty = re.findall(r'\d+|[A-z]+',s)
print(hodnoty)
cisla = []
sustava = []
for i in range(len(hodnoty)):
    if i % 2 ==0:
        cisla.append(hodnoty[i])
    else:
        sustava.append(hodnoty[i])

for i in range(len(cisla)):
    if sustava[i] == '2':
        print(cisla[i],' - ', int(cisla[i],2))
    if sustava[i] == '8':
        print(cisla[i],' - ',int(cisla[i],8))
    if sustava[i] == '16':
        print(cisla[i],' - ',int(cisla[i],16))


