#!/usr/bin/env python3.10

from math import sqrt, factorial

def main():
    numbers = [ 'Nul','Een','Twee','Drie','Vier','Vijf', 
                'Zes', 'Zeven', 'Acht', 'Negen', 'Tien',
                'Elf', 'Twaalf', 'Dertien', 'Veertien',
                'Vijftien', 'Zestien', 'Zeventien', 
                'Achttien', 'Negentien', 'Twintig'] 
    calculations = [
        44-44, 
        44/44, 
        (44+4)/factorial(4), 
        (4*4-4)/4, 
        4+4*(4-4),
        (4*4+4)/4, 
        (4+4)/4+4, 
        4+4-4/4, 
        4/4*4+4, 
        4/4+4+4, 
        (4+4+4)-sqrt(4),
        (factorial(4)*sqrt(4)-4)/4, 
        4*(4-4/4), 
        (factorial(4)*sqrt(4) +4)/4,
        4*4-4/sqrt(4), 
        4*4-4/4, 
        4*4+4-4, 
        4*4+4/4, 
        4*4+4-sqrt(4), 
        factorial(4)-(4+4/4), 
        4*(4 / 4 + 4)
    ]

    for num, calc in zip(numbers, calculations):
        print(f'{num} is {int(calc)}')


if __name__ == '__main__':
    main()
