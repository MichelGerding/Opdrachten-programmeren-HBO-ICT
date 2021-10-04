# Programmeren I, Week 3 Opgave 3
# Bestandsnaam: wk3ex3.py
# Naam:
# Probleemomschrijving: List comprehensions


# hiermee krijgen we functies als sin en cos...
from math import *

# twee extra functies (die niet in de module math hierboven zitten)


def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2 * x


def sq(x):
    """Squarer!  argument: x, a number"""
    return x ** 2


# voorbeelden om aan list comprehensions te wennen...


def lc_mult(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each multiplied by 2**
    """
    return [2 * x for x in range(n)]


def lc_idiv(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    # return [x // 2 for x in range(n)]
    return [float(x // 2) for x in range(n)]


def lc_fdiv(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x / 2 for x in range(n)]


assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0.0, 0.0, 1.0, 1.0]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]


# Hier begin je met de functies voor deze opgave:


# Stap 1, deel 1
def unitfracs(n):
    """This function takes a integer n and calculates
        all fractions of n and returns them in a list for example 
        n =5
        return [1/5, 2/5, 3/5, 4/5] 
    """
    return [(1/n)*i for i in range(n)]

def interp(low, hi, fraction):
    """Returns a value frac of the way from low to hi"""
    return low + (hi - low) * fraction


def scaledfracs(low, hi, n):
    """ this function returns the the fractions of n scaled between
        a top and bottom value. without the upper bound
        Arguments:  low the lowerbound of the range
                    hi the upperbound of the range
                    n the number of fractions
        Return value: a list of floats
    """
    return [interp(low, hi, x) for x in unitfracs(n)]
assert scaledfracs(0,1,4) == [0.0, 0.25, 0.5, 0.75] 
assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
assert scaledfracs(41, 43, 8) == [41.0, 41.25,
                                  41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5] 

def sqfracs(low, hi, n):
    return [x**2 for x in scaledfracs(low,hi,n)]


# 5 tests for sqfracs
assert sqfracs(0,1,4) == [0.0, 0.0625, 0.25, 0.5625]
assert sqfracs(10, 30, 5) == [100.0, 196.0, 324.0, 484.0, 676.0]
assert sqfracs(41, 43, 8) == [1681.0, 1701.5625, 1722.25, 1743.0625, 1764.0, 1785.0625, 1806.25, 1827.5625]
assert sqfracs(0, 10, 4) == [0.0, 6.25, 25.0, 56.25]
assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]

def f_of_fracs(f, low, hi, n):
    """ this function runs the passed function on the scaled fractions of low, hi, n
    
        Arguments:  f, a function
                    low, number, lower bound of the range
                    hi the upperbound of the range
                    n the number of fractions
        Return value: a list of floats
    """
    return [f(i) for i in scaledfracs(low, hi, n)]


assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
assert f_of_fracs(sin, 0, pi, 2) == [0.0, 1.0] 
assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]


def integrate(f, low, hi, n):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where n steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of n uniform steps
       from low to hi
    """
    return sum(f_of_fracs(f, low, hi, n)) * (hi - low) / n

assert integrate(dbl, 0, 10, 4) == 75
assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])


""" Vraag 1.

de functie integrate maakt altijd een onderschatting want je neemt de waarde
als hoogte voor de linke kant van de vakken en telt dat ij elkaar op
daardoor zijn er altijd niet megerekende vakken
"""


def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x ** 2) ** 0.5


print(integrate(c, 0, 2, 2))
print(integrate(c, 0, 2, 20))

""" Vraag 2. 

als de waarde van n in de functie integrate gaat de waarde steeds dichter 
naar de waarde van pi want dat is de  

"""
