print("Henkilö 1:")

nimi = input("Nimi: ")
ika = int(input("Ikä: "))
print("Henkilö 2: ")
nimi2 = input("Nimi: ")
ika2 = int(input("Ikä: "))

if ika > ika2:
    print(f"Vanhempi on {nimi}")
elif ika < ika2:
    print(f"Suurempi luku: {nimi2}")
elif ika == ika2:
    print(f"{nimi} ja {nimi2} ovat yhtä vanhoja")