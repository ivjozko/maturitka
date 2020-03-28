import re
filee = open('hada.txt','r').read()
new_file = re.sub(r'\n',' ',filee)
lst = re.findall(r'[HDLP]+',new_file)
print('pocet hier =',len(lst))
c = 1
mx = 0
mxx = 0
for game in lst:
    if len(game) > mx:
        mx = len(game)
        mxx = c
    c+=1
print('najdlhsia hra =',mxx,' s poctom znakov =',mx)
for i in lst:
    h = re.findall(r'H',i)
    d = re.findall(r'D',i)
    l = re.findall(r'L',i)
    p = re.findall(r'P',i)
    hh = len(h)
    dd = len(d)
    ll = len(l)
    pp = len(p)
    print('H',hh,' D',dd,' P',pp,' L',ll)
