x = int(input("Montako kertaa viikossa syöt Unicafessa? "))
y = float(input("Unicafe-lounaan hinta? "))
z = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

day = round(((x*y+z)/7), 2)

print(f"""Kustannukset keskimäärin:
Päivässä {day} euroa
Viikossa {x*y+z} euroa""")
