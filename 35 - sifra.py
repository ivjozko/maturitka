f = open('zachyt.txt','r').read()
text = ''
znaky = [' ','.',',','!','?']
for i in f:
    for pismeno in i:
        if pismeno in znaky:
            pass
        else:
            pismeno = chr(ord(pismeno)-1)
        text+=pismeno
print(text)

'''
xd = open('rozsifrovane.txt','a')
xd.write(text)'''