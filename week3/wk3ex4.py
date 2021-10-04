"""
dit bestandt voegt extra functionaliteit toe aan svtree 
door een wilekeurig meer realistischere boom te maken 
"""
import random
from turtle import Turtle, Screen, tracer, update

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500

# setup the screen
screen = Screen()
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT, 'white')
screen.colormode(255)
#setup the turtle
t = Turtle(shape='turtle')
t.speed(0)
t.penup()
t.sety(-SCREEN_HEIGHT/2)
t.setheading(90)
t.pendown()
tracer(0,0)
def svtree(t, trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    width = 10 * (levels/10)
    zip
    angle = random.randrange(5, 20) if random.randint(0, 30) != 2 else random.randrange(50,80)
    if levels == 0:
        return
    elif levels < 2 and random.randint(0, 10) == 3:
        levels -= 2
    else:
        if levels < 2:
            t.color((66,105,47))
            width *= 2
        else: 
            t.color((114,92,66))
        t.width(width) 
        # Teken de oorspronkelijke stam (1 regel)
        t.forward(trunklength)
        # Draai een stukje om de eerste subboom te positioneren (1 regel)
        t.left(angle)
        # Voer recursie uit! met een kleinere stam en minder niveaus (1 line)
        svtree(t, trunklength*0.8, levels-1)
        t.right(angle)

        # Draai de andere kant op om de tweede subboom te positioneren (1 regel)
        t.right(angle)

        # Voer opnieuw recurs4ie uit! (1 regel)
        svtree(t, trunklength*0.8, levels-1)
        # Draai en ga TERUG (2 stappen: 2 regels)
        t.left(angle)
        t.penup()
        t.backward(trunklength)
        t.pendown()
        
        update()

svtree(t, 100, 10)

input()
