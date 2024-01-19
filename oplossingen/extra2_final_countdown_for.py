# Schrijf een programma dat:
# - de gebruiker vraagt om een positief geheel getal in te voeren
# - een countdown uitvoert vanaf het gekozen getal tot 0. Deze keer niet met een while-lus!
getal = int(input("Voer een positief geheel getal in: "))

for i in range(getal, -1, -1):
    print(i)