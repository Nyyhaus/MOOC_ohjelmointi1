opiskelijat_lkm = int(input("Montako opiskelijaa? "))
ryhmän_koko = int(input("Mikä on ryhmän koko? "))

jakojäännös = opiskelijat_lkm % ryhmän_koko

if jakojäännös != 0:
    ryhmien_määrä = opiskelijat_lkm // ryhmän_koko + 1 
    print(f"Ryhmien määrä: {ryhmien_määrä}")
else:
    ryhmien_määrä = opiskelijat_lkm // ryhmän_koko 
    print(f"Ryhmien määrä: {ryhmien_määrä}")