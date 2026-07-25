#Programmbeginn Taschenrechner
rechenart = str(input("Welche Rechenart möchtest du benutzen"))
zahl1 = float(input("Erste Zahl eingeben"))
zahl2 = float(input("Zweite Zahl eingeben"))
if rechenart == "+":
    result = zahl1 + zahl2
    print(result)
elif rechenart == "-":
    result = zahl1 - zahl2
    print(result)
elif rechenart == "*":
    result = zahl1 * zahl2
    print(result)
elif rechenart == "/":
    result = zahl1 / zahl2
    print(result)
else:
    print("Dies ist kein gültiger Operator, Berechnung konnte nicht durchgeführt werden")