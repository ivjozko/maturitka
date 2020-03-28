import re
subor = open('bus_vytazenost.txt','r').read()
zastavky = re.findall(r'[A-z]+[ ][A-z]+|[A-z]+',subor)
print(zastavky)
print("Pocet zastavok",len(zastavky))
nastup = re.findall(r'[0-9]+',subor)

mx = int(nastup[0])
zmena = 1
obsadenost = 0
nad = 0
max_nad = 0
for i in range(len(zastavky)):
    obsadenost = obsadenost + int(nastup[zmena]) - int(nastup[zmena+1])
    zmena += 2
    if obsadenost > mx:
        print("Preplneny bus po zastavke",zastavky[i],".")
        nad = obsadenost - mx
        if nad > max_nad:
            max_nad = nad
print(max_nad)
