ikä = int(input("Kerro ikäsi? "))

if 5 <= ikä <= 120:
    print(f"Ok, olet siis {ikä}-vuotias")
elif 0 < ikä < 5:
    print("En usko, että osaat kirjoittaa...")
else:
    print("Taitaa olla virhe")