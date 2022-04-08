lahja = int(input("Lahjan suuruus? "))

if lahja < 5000:
    print("Ei veroa!")
elif 5000 <= lahja < 25000:
    vero = (100 + (lahja-5000) * 0.08)
    print(f"Vero: {vero}")
elif 25000 <= lahja < 55000:
    vero = (1700 + (lahja-25000) * 0.1)
    print(f"Vero: {vero}")
elif 55000 <= lahja < 200000:
    vero = (4700 + (lahja-55000) * 0.12)
    print(f"Vero: {vero}")
elif 200000 <= lahja < 1000000:
    vero = (22100 + (lahja-200000) * 0.15)
    print(f"Vero: {vero}")
elif lahja > 1000000:
    vero = (142100 + (lahja-1000000) * 0.17)
    print(f"Vero: {vero}")