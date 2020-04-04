hmotnost = []
vyska = []
index = []
def bmi():
    global hmotnost,vyska,index
    while True:
        hmotnost.append(int(input('Davaj hmotnost: ')))
        vyska.append(int(input('Davaj vysku: ')))
        index.append(hmotnost[-1]-(vyska[-1]-100))
        a = input('Pokracuj')
        if a == 'nie':
            break
    nadvaha = 0
    podvaha = 0
    neutral = 0
    for i in range(len(index)):
        if index[i] > 5:
            nadvaha += 1
        elif index[i] < -10:
            podvaha += 1
        else:
            neutral += 1

    n = (nadvaha*100/len(index))
    p = (podvaha*100/len(index))
    g = (neutral*100/len(index))
    return('nadvaha:', round(n,2),'%', 'podvaha:', round(p,2),'%', 'chill:', round(g,2),'%')

print(bmi())