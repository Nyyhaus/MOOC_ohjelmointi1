luku = int(input("Anna luku: "))
if luku < 1000 and luku > 100:
    print("Luku on pienempi kuin 1000")
elif luku < 100 and luku < 1000 and luku > 10:
    print("Luku on pienempi kuin 1000")
    print("Luku on pienempi kuin 100")
elif luku < 10 and luku < 100 and luku < 1000:
    print("Luku on pienempi kuin 1000")
    print("Luku on pienempi kuin 100")
    print("Luku on pienempi kuin 10")
print("Kiitos!")