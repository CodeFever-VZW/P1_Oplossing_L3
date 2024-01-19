# Schrijf een programma dat:
# - de gebruiker vraagt om een positief geheel getal in te voeren
# - een countdown uitvoert vanaf het gekozen getal tot 0
getal = int(input("Voer een positief geheel getal in: "))
while getal >= 0:
    print(getal)
    getal -= 1