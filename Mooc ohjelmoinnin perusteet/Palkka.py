tuntipalkka = float(input("Tuntipalkka: ")) 
työtunnit = int(input("Työtunnit: "))
viikonpäivä = input("Viikonpäivä: ")

palkka = tuntipalkka * työtunnit


if viikonpäivä == "sunnuntai":
    palkka = palkka * 2


print(f"Palkka {palkka} euroa")

