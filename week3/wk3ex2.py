# Programmeren I, week 3 opgave 2
# Bestandsnaam: wk3ex2.py
# Naam:
# Probleemomschrijving: Slaapwandelende student

import random
from statistics import mean

def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nstep): 
    print(f'start is {start}')
    if nstep == 0:
        return start
    return rwpos(start + rs(), nstep-1)


def rwpos_plain(start, nstep):
    if nstep == 0:
        return start
    return rwpos_plain(start + rs(), nstep-1)

def cabs(num):
    return -num if num < 0 else num

def ave_signed_displacement(numtrials):
    return mean([cabs(rwpos_plain(0, 100)) for i in range(numtrials)])


def ave_squared_displacement(numtrials):
    return mean([cabs(rwpos_plain(0, 100)**2) for i in range(numtrials)])


class Charray(list):

    def __init__(self, mapping=[]):
        "A character array."
        if type(mapping) in [int, float]:
            mapping = str(mapping)
        list.__init__(self, mapping)

    def __getslice__(self, i, j):
        return Charray(list.__getslice__(self, i, j))

    def __setitem__(self, i, x):
        if type(x) != str or len(x) > 1:
            raise TypeError
        else:
            list.__setitem__(self, i, x)

    def __repr__(self):
        return "charray['%s']" % self

    def __str__(self):
        return "".join(self)

def print_message(low, high, loc):
    board_width = high - low
    corrected_loc = loc - low
    board = Charray('|' + '-'*board_width + '|')
    board[corrected_loc] = 'S'
    print(''.join(board))


def rwsteps(start, low, hi, index=0):
    if start >= hi or start <= low:
        return index
    print_message(low, hi, start)
    next_pos = start + rs() 
    return rwsteps(next_pos, low, hi, index+1)


# print(rwpos(40, 4))
# print(rwsteps(10, 5, 15))

# print(ave_signed_displacement(10000))
# print(ave_squared_displacement(10000))


"""
    Om de gemiddelde totale afwijking voor een
    toevalsbeweging met 100 willekeurige stappen
    te berekenen, heb ik ... door middel van list comprehension 
    de functie ave_signed_displacement 10000 keer uitgevoerd
    het resultaat van elke functie call word de min teken 
    erafgehaald en daarna in een list gestopt. zodra alle results 
    in een list zitten dan wordt de functie `statistics.mean` uitgevoerd
    om het gemiddelde te berekenen.
    daaruit is gekomen dat hij gemiddeld 7-8 stappen van het begin verwijderdt 
    raakt 

    Zorg dat je ave_signed_displacement en
    ave_squared_displacement beide ten minste één
    keer uitvoert en de gegevens en het gemiddelde
    hierin kopieert.

    ave_signed_displacement: 7.618
    ave_squared_displacement: 98.028
"""
