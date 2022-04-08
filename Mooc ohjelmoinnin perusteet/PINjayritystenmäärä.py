yritykset = 0

while True:
    pin = int(input("PIN-koodi: "))
    yritykset += 1
    if pin != 4321:
        print("Väärin")
    else:
        if yritykset == 1:
            print("Oikein, tarvitsit vain yhden yrityksen!")
        else:
            print(f"Oikein, tarvitsit {yritykset} yritystä")
            break