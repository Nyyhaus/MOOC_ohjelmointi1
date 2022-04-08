sana = input("Sana: ")
merkki = input("Merkki: ")
osajono = " "

while True:
    kohta = sana.find(merkki)
    if kohta == -1:
        break
    if kohta < len(sana) - 2:
        if osajono in sana:
            sana = sana[1:]
            continue
        print(sana[kohta:kohta + 3])
        osajono = sana[kohta:kohta + 3]
        sana = sana[1:]

    else:
        break