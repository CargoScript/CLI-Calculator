aktuelles_Ergebnis = None

while True:
    if aktuelles_Ergebnis == None:
        try:
            zahl1 = float(input("Erste Zahl eingeben"))
        except ValueError:
            print(("Bitte gib eine Zahl statt einem Zeichen ein"))
            continue
    else:
        zahl1 = aktuelles_Ergebnis
        print(f"Wir rechnen weiter mit {zahl1}")
    rechenart = str(input("Welche Rechenart möchtest du benutzen"))
    try:
        zahl2 = float(input("Zweite Zahl eingeben:"))
    except ValueError:
        print(("Bitte gib eine Zahl statt einem Zeichen ein"))
    erfolgreich_berechnet = True

    if rechenart == "+":
        result = zahl1 + zahl2

    elif rechenart == "-":
        result = zahl1 - zahl2

    elif rechenart == "*":
        result = zahl1 * zahl2

    elif rechenart == "/":
        result = zahl1 / zahl2

    else:
        print("Kein gültiger Operator")
        erfolgreich_berechnet = False

    if erfolgreich_berechnet:
        print(f"Ergebnis: {result}")
        aktuelles_Ergebnis = result
    else:
        print("Berechnung übersprungen. Versuche es noch einmal")

    auswahl = input("Weiterrechnen (w), Neue Berechnung (n), Programm beenden (e)")
    if auswahl.lower() == "e":
        print("Vielen Dank für die Nutzung des Taschenrechners,bis zum nächsten mal")
        break
    elif auswahl.lower() == "n":
        aktuelles_Ergebnis = None
