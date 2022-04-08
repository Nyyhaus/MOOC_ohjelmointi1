luku = int(input("Mihin asti: "))
# kerroin = int(input("Mikä kerroin: "))

i = 0
j = 0
lasku = ""

while i <= luku:
    i = i + j
    j += 1
    if j <= luku: 
        lasku += f"{j}"
        if j < luku:
            lasku += " + "

print(f"Laskettiin {lasku} = {i}")