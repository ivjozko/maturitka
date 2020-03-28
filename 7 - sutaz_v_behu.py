subor = open("sutaz_v_behu.txt","r")
suborik = subor.readlines()

vsetko = []

for line in suborik:
    pole = line.strip().split(" ")
    vsetko.append(pole)

print("Pocet zucastnenych sportovcov:",len(vsetko))

minn = 1000000
meno = ''
for i in range (len(vsetko)):
    print("Sutaziaci",vsetko[i][0],"dobehol do ciela za",vsetko[i][1],"sekund.")
    if int(vsetko[i][1]) < int(minn):
        minn = int(vsetko[i][1])
        meno = vsetko[i][0]

print("Vyhral",meno,"s casom",minn//60,"minut a",minn%60,"sekund," )





