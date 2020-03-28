vyska = int(input("Zadaj vysku v metroch z akej hadzes loptu: "))
koeficient = int(input("Zadaj koeficient odrazu v precentach: "))/100

vacsie_ako_meter = 0
for i in range (11):
    if vyska >= 1:
        vacsie_ako_meter += 1
    print(i,":","%.2f" % vyska,"m")
    vyska = vyska*koeficient
print(vacsie_ako_meter,"krat vyskocila vyssie ako 1 meter")
