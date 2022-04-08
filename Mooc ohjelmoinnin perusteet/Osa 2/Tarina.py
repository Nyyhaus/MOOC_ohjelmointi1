from queue import Empty


sana = ""
sanat = ""

while sana != "loppu":
    sana = input("Anna sana: ")
    if sana == "loppu":
        break
    if sanat != "":
        print(sanat[:-len(sana)])

        if sana == sanat[-2]:
            break
    sanat += sana + " "

print(sanat)