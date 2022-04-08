kirjain1 = input("Anna 1. kirjain: ")
kirjain2 = input("Anna 2. kirjain: ")
kirjain3 = input("Anna 3. kirjain: ")

if kirjain1 > kirjain2 and kirjain1 < kirjain3:
    print(f"Keskimmäinen kirjain on {kirjain1}")
if kirjain1 > kirjain3 and kirjain1 < kirjain2:
    print(f"Keskimmäinen kirjain on {kirjain1}")
elif kirjain2 < kirjain1 and kirjain2 > kirjain3:
    print(f"Keskimmäinen kirjain on {kirjain2}")
elif kirjain2 > kirjain1 and kirjain2 < kirjain3:
    print(f"Keskimmäinen kirjain on {kirjain2}")
elif kirjain3 > kirjain1 and kirjain3 < kirjain2:
    print(f"Keskimmäinen kirjain on {kirjain3}")
elif kirjain3 < kirjain1 and kirjain3 > kirjain2:
    print(f"Keskimmäinen kirjain on {kirjain3}")
