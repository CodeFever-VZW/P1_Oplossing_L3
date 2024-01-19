# Maak een selectie om na te gaan of iemand oud genoeg is voor een rijbewijs.
def check_rijbewijsleeftijd(leeftijd):
    rijbewijsleeftijd = 18

    if leeftijd >= rijbewijsleeftijd:
        print("Je bent oud genoeg voor een rijbewijs!")
    else:
        print("Je bent nog te jong voor een rijbewijs.")

# Vraag de leeftijd aan de gebruiker
input_leeftijd = int(input("Hoe oud ben je? "))

# Roep de functie aan om de leeftijd te controleren
check_rijbewijsleeftijd(input_leeftijd)