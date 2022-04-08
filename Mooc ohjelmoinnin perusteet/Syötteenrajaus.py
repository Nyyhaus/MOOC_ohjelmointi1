from math import sqrt

luku = int(input('Syötä luku: '))


while luku != 0:
    if luku > 0:
        print(sqrt(luku))
    elif luku < 0:
        print("Epäkelpo luku")
    luku = int(input('Syötä luku: '))

print("Lopetetaan...")