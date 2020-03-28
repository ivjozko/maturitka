subor = open('sms.txt','r').read()

subor = list(subor)

for i in range(len(subor)):
    if str(subor[i - 1]) == '\n':
        subor[i] = (subor[i]).upper()
    if str(subor[i - 1]) == '':
        subor[i] = (subor[i]).upper()
    if str(subor[i]) == ' ':
       subor[i] = ''


print("".join(subor))

