weight=int(input("Enter weight:"))
unit=input("Is it in (L)bs or (K)g:")
if unit.upper()=='L':
    converted = weight*0.45
    print(f"Your are {converted} Kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} Pounds")
