# Schrijf een programma dat een vierkant tekent met de turtle - module.
# - import turtle
# - maak een functie teken_lijn(lengte)
# - maak een functie draai_rechts(graden)
# - maak een functie teken_vierkant()
#     - gebruik een lus om vier zijdes te tekenen
# - gebruik turtle.done() zodat je jouw tekening kan zien.
import turtle
def teken_lijn(lengte):
    turtle.forward(lengte)

def draai_rechts(graden):
    turtle.right(graden)

def teken_vierkant():
    for _ in range(4):
        teken_lijn(100)
        draai_rechts(90)


teken_vierkant()

turtle.done()