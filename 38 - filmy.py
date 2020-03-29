import re
subor = open('nfilmov.txt','r').read()

mena = re.findall(r'[A-z]+[ ][A-z]+[ ][A-z]+[ ][A-z]+[ ][A-z]+[ ][A-z]+|[A-z]+[ ][A-z]+[ ][A-z]+[ ][A-z]+|[A-z]+[ ][A-z]+|[A-z]+',subor)
print(mena)
cisla = re.findall(r'[0-9]+',subor)
print(cisla)

navs_arr = []
film_arr = []
mena_arr = []
for i in range(int(len(mena)/2)):
    i *= 4
    navstevovanost = int(cisla[i]) + int(cisla[i+1]) + int(cisla[i+2]) + int(cisla[i+3])
    navs_arr.append(navstevovanost)
    i /= 4
    i = int(i) * 2
    print("Pre film",mena[i],"bola navstevovanost",navstevovanost)
    film_arr.append(mena[i])
    mena_arr.append(mena[i+1])

zoradene = [x for _, x in sorted(zip(navs_arr,film_arr))]
print("Zoradene filmy od najmenej po najviac navstevovane: ")
print(zoradene)

zoradene.reverse()
for i in range(10):
    print(zoradene[i],navs_arr[i])

vstup = input("Zadaj meno herca a ja ty poviem ake filmy: ")

poc = 0
for i in range(len(mena_arr)):
    if mena_arr[i] == vstup:
        print(film_arr[i])
        poc += 1
print("Dokopy {} filmy.".format(poc))