x = [0,2000,2500,2000,1500,2000]
y = [185,204,258,207,156,220]
print('Najnizsia nadmorska vyska',min(y),'m.n.m.')
print('Najvissia nadmorska vyska',max(y),'m.n.m.')
print('Dlzka trasy',sum(x),'m.')

file = open('tur_trasa.txt','w')
file.write(str(min(y)))
file.write(' ')
file.write(str(max(y)))
file.write(' ')
file.write(str(sum(x)))
file.write(' ')