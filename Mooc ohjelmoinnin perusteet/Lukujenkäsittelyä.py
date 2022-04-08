# print("Syötä kokonaislukuja, 0 lopettaa:")
luku = ""
summa = 0
lukujen_määrä = 0
negatiivinen = 0
positiivinen = 0

while luku != 0:
    luku = int(input("Luku: "))
    if luku != 0:
        if luku > 0:
            positiivinen += 1
        else:
            negatiivinen += 1
        lukujen_määrä += 1
        summa = summa + luku
        keskiarvo = (summa/lukujen_määrä)
    

print(f"Lukuja yhteensä {lukujen_määrä}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {keskiarvo}")
print(f"Positiivisia {positiivinen}")
print(f"Negatiivisia {negatiivinen}")