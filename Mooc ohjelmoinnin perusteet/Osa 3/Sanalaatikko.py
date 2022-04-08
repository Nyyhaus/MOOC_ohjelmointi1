sana = input("Sana: ")

tähdet = 20 - len(sana)

if len(sana) % 2 == 0:
    tyhjää = 14-int(len(sana)/2)
    print(30*"*")
    print("*"+" "*tyhjää+sana+" "*tyhjää+"*")
    print(30*"*")
else:
    tyhjää = 13-int(len(sana)/2)
    print(30*"*")
    print("*"+" "*tyhjää+sana+" "*tyhjää+" "+"*")
    print(30*"*")
