sana = input("Salasana: ")

while True:

    salasana = input("Toista salasana: ")
    if salasana != sana:
        print("Ei ollut sama!")
    elif salasana == sana:
        print("Käyttäjätunnus luotu!")
        break
