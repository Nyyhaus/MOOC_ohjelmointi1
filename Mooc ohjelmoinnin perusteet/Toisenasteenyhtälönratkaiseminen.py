from math import sqrt

a = int(input("Anna a: "))
b = int(input("Anna b: "))
c = int(input("Anna c: "))

juuri1 = (-b+sqrt(b**2-4*a*c))/(2*a)
juuri2 = (-b-sqrt(b**2-4*a*c))/(2*a)

print(f"Juuret ovat {juuri1} ja {juuri2}")