import re
subor = open('sifro.txt','r').read()
subor1 = open('frekv.txt','r').read()

znaky =  re.findall(r'.',subor)
frekv_znaky = re.findall(r'[A-z]|[.]|[,]|[ ]',subor1)
frekv_hodnoty = re.findall(r'[0-9]+',subor1)
text = re.findall(r'.+',subor)

v_celku = [text[0]+text[1]+text[2]+text[3]+text[4]+text[5]+text[6]+text[7]+text[8]]


spocitane = []
poc = 0
for i in range(100):
    if chr(i+33) in znaky:
        poc = znaky.count(chr(i+33))
    if poc == 0:
        pass
    else:
        spocitane.append(chr(i+33))
        spocitane.append(poc)
    poc = 0

sifro_znaky = []
sifro_hodnoty = []
for i in range(len(spocitane)):
    if i % 2 == 0:
        sifro_znaky.append(spocitane[i])
    if i % 2 != 0:
        sifro_hodnoty.append(spocitane[i])

frekv_hodnoty =[int(i)for i in frekv_hodnoty]

zoradene_sifro = [x for _, x in sorted(zip(sifro_hodnoty,sifro_znaky))]

zoradene_frekv = [z for _, z in sorted(zip(frekv_hodnoty,frekv_znaky))]

rozkuskovane = []
for i in v_celku:
    for j in i:
        rozkuskovane.append(j)

preklad = []
for i in range(len(rozkuskovane)):
    preklad.append(zoradene_frekv[zoradene_sifro.index(rozkuskovane[i])])

print(spocitane)
print("".join(preklad))

file = open('kluc.txt','a')
file.write(str(zoradene_sifro))
file.write('\n')
file.write(str(zoradene_frekv))
