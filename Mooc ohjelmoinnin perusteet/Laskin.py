luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
komento = input("Komento: ")

if komento == "summa":
    summa = luku1 + luku2
    print(f"{luku1} + {luku2} = {summa}")
if komento == "erotus":
    summa = luku1 - luku2
    print(f"{luku1} - {luku2} = {summa}")
if komento == "tulo":
    summa = luku1 * luku2
    print(f"{luku1} * {luku2} = {summa}")