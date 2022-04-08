print("Kerro huominen sääennuste:")
lämpötila = int(input("Lämpötila: "))
sade = input("Sataako (kyllä/ei): ")

if lämpötila > 20 and sade == "ei":
    print("Pue housut ja t-paita")
elif lämpötila > 20 and sade == "kyllä":
    print("Pue housut ja t-paita\nMuista sateenvarjo!")
elif lämpötila <= 20 and lämpötila > 10 and sade == "ei":
    print("Pue housut ja t-paita\nOta myös pitkähihainen paita")
elif lämpötila <= 20 and lämpötila > 10 and sade == "kyllä":
    print("Pue housut ja t-paita\nOta myös pitkähihainen paita\nMuista sateenvarjo!")
elif lämpötila <= 10 and lämpötila > 5 and sade == "ei":
    print("Pue housut ja t-paita\nOta myös pitkähihainen paita\nPue päälle takki")
elif lämpötila <= 10 and lämpötila > 5 and sade == "kyllä":
    print("Pue housut ja t-paita\nOta myös pitkähihainen paita\nPue päälle takki\nMuista sateenvarjo!")
elif lämpötila <= 5 and sade == "kyllä":
    print("""Pue housut ja t-paita\n
Ota myös pitkähihainen paita\n
Pue päälle takki\n
Suosittelen lämmintä takkia\n
Kannattaa ottaa myös hanskat\n
Muista sateenvarjo!""")
elif lämpötila <= 5 and sade == "ei":
    print("""Pue housut ja t-paita\n
    Ota myös pitkähihainen paita\n
Pue päälle takki\n
Suosittelen lämmintä takkia\n
Kannattaa ottaa myös hanskat\n""")
