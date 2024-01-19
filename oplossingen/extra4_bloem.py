# Teken een bloem met Turtle.
#
# Tip: Begin met het tekenen van een enkele bloemblaadje.
#
# - Gebruik een lus om hetzelfde bloemblaadje meerdere keren te tekenen
# - Draai de Turtle na elke iteratie een beetje om een volledige bloem te creëren
import turtle

def teken_bloemblaadje():
    for i in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)

def teken_bloem():
    for i in range(6):
        teken_bloemblaadje()
        turtle.right(60)

teken_bloem()

turtle.done()