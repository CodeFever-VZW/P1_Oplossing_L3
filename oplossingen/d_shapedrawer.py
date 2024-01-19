# Maak een programma dat de gebruiker in staat stelt een vorm te kiezen (vierkant, driehoek of cirkel)
# en de gekozen vorm op het scherm te tekenen.
#
# Als de gebruiker een ongeldige vorm invoert, moet het programma een foutmelding weergeven.

import turtle
import time


def teken_vierkant():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def teken_driehoek():
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

def teken_cirkel():
    turtle.circle(50)

def kies_vorm():
    user_input = turtle.textinput("tekenaar", "Kies een vorm.  Geldige vormen zijn: vierkant, driehoek of cirkel.") or ''
    return user_input.lower()

def toon_foutmelding():
    turtle.penup()
    turtle.goto(-100, -200)
    turtle.pendown()
    turtle.write("Foute input! Kies een correcte vorm.", align="left", font=("Arial", 16, "normal"))

def wis_veld():
    time.sleep(5)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.clear()

def maak_veld():
    turtle.setup(500, 500)
    turtle.title("tekenaar")
    turtle.speed(1)

def teken_vorm():
    vorm = kies_vorm()

    if vorm == "vierkant":
        teken_vierkant()
    elif vorm == "driehoek":
        teken_driehoek()
    elif vorm == "cirkel":
        teken_cirkel()
    else:
        toon_foutmelding()


def start_teken_programma():
    maak_veld()
    while True:
        teken_vorm()
        wis_veld()


# Start het programma
start_teken_programma()