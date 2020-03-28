import re
subor = open('bin.txt','r').read()
binar = re.findall(r'[0-1]+',subor)

for i in binar:
    print(i,'-',int(i, 2))