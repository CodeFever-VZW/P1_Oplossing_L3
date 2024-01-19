# Schrijf een programma dat:
# - de gebruiker vraagt om een getal in te voeren
# - controleert of het getal even of oneven is
# - zegt aan de gebruiker of het getal even of oneven is
#
# Voor deze oefening kan je de modulo - operator goed gebruiken.
# Die wordt weergegeven door het symbool ‘ % ’ en berekent de restwaarde na de deling.
#
# Bijvoorbeeld: 17 % 5 geeft 2.
getal = int(input("Voer een getal in: "))
if getal % 2 == 0:
    print("Het ingevoerde getal is even.")
else:
    print("Het ingevoerde getal is oneven.")