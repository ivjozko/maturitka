cesty = [[0, 1, 2, 3, 4], [1, 0, 1, 0, 2], [2, 1, 0, 2, 1], [3, 0, 2, 0, 2],[4, 2, 1, 2, 0]]

for riadok in cesty:
    for prvok in riadok:
        print('', prvok, end='  ')
    print()

bez_cest = []
jed_cest = []
dva_cest = []
for i in range(1,4):
    for j in range(i+1,5):
        if  cesty[i][j] == 0:
            bez_cest.append(i)
            bez_cest.append(j)
        if cesty[i][j] == 1:
            jed_cest.append(i)
            jed_cest.append(j)
        if cesty[i][j] == 2:
            dva_cest.append(i)
            dva_cest.append(j)

for i in range(0,len(bez_cest),2):
    print("Cesta nieje medzi mestami: ",bez_cest[i],'a',bez_cest[i+1])

for i in range(0,len(jed_cest),2):
    print("Jednosmerka je medzi mestami: ",jed_cest[i],'a',jed_cest[i+1])

for i in range(0,len(dva_cest),2):
    print("Dvojsmerka je medzi mestami: ",dva_cest[i],'a',dva_cest[i+1])
