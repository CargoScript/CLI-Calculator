

rechenart = str(input("Welche Rechenart möchtest du benutzen:"))
zahl1 = float(input("Gebe die erste Zahl mit der du rechnen möchtest ein:"))
zahl2 = float(input("Gebe die zweite Zahl mit der du rechnen möchtest ein:"))
if rechenart == '+':
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1 + zahl2} ")
elif rechenart == '-':
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1 - zahl2}" )
elif rechenart == '*':
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1 * zahl2}" )
elif rechenart == '/':
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1 / zahl2}" )
else:
    print("Kein gültiger Operator")
