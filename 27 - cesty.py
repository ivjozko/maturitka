import re
subor = open("cesty.txt","r").read()
cesty = re.findall(r'[0-9]+',subor)

dokopy = 0
x = 0
y = 1
maxi = 0
xo = 0
yo = 0
for i in cesty:
    dokopy += int(i)
    x += 1
    if int(i) > maxi:
        maxi = int(i)
        xo = x
        yo = y
    if x == 5:
        x = 0
        y += 1


vysledok = dokopy/2
print(vysledok)
print("Najvacsia vzdialenost je medzi dedinou",xo ,"a",yo)