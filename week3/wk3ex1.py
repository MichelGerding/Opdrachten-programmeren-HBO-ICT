from turtle import *
from random import *

speed(0)

def tri(n):
    if n == 0:
        return
    else:
        forward(100)
        left(120)
        tri(n-1)



def spiral(initial_length, angle, multiplier):
    """Spiral-drawing function.  Arguments:
       initial_length = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    if initial_length <= 1:          
        return      # Niets meer te tekenen, dus beëindig deze aanroep naar spiral
    else:
        forward(initial_length)
        left(angle)
        spiral(initial_length * multiplier, angle, multiplier)


def chai(size):
    """Our chai function!"""
    if size < 5: 
        return
    else:
        forward(size)
        left(90)
        forward(size/2)
        right(90)
        chai(size/2)

        right(90)
        forward(size)
        left(90)
        chai(size/2)

        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

def svtree(trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    angle = 30
    if levels == 0:
        return
    else:
        # Teken de oorspronkelijke stam (1 regel)
        forward(trunklength)
        # Draai een stukje om de eerste subboom te positioneren (1 regel)
        left(angle)
        # Voer recursie uit! met een kleinere stam en minder niveaus (1 line)
        svtree(trunklength/2, levels-1)
        right(angle)
        
        # Draai de andere kant op om de tweede subboom te positioneren (1 regel)
        right(angle)
    
        # Voer opnieuw recursie uit! (1 regel)
        svtree(trunklength/2, levels-1)
        # Draai en ga TERUG (2 stappen: 2 regels)
        left(angle)
        backward(trunklength)



def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)


def flakeside(length, levels):
    
    if levels == 0:
        forward(length)
        return 
    elif levels == 1:
        length /= 3
        forward(length)
        right(60) 
        flakeside(length, levels - 1)
        left(120) 
        flakeside(length , levels - 1)
        right(60) 
        forward(length)
        
    else: 
        length /= 3
        flakeside(length, levels - 1)
        right(60) 
        flakeside(length , levels - 1)
        left(120)
        flakeside(length , levels - 1)
        right(60) 
        flakeside(length , levels - 1)
        

color('red')
snowflake(300, 0)
color('black')
snowflake(300, 1)
color('pink')
snowflake(300, 2)
color('orange')
snowflake(300, 3)
