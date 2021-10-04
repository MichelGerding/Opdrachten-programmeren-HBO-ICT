from random import randint


def main():
    # maak een list met keuzes
    # de list is gesoorteerd op volgorde van wat wint van wat
    # input  
    choices = ['steen','schaar', 'papier']
    # loop voor altijd
    while True: 
        comp_choice = randint(0, len(choices) -1)

        # we pakken de input van de gebruiker. dit is of een nummer 
        try: 
            user_choice = get_user_pick(choices)
            
            # kijk of the gebruiker wint. geeft None terug bij gelijk spel. hierbij geven we mee het aantal keuzes,
            # de keuze van de computer en de keuze van de speler
            user_won = has_user_won(user_choice-1, comp_choice, total_choices=len(choices))

            win_message = get_win_message(user_won)
            
            print(f'''
jij koos: {choices[user_choice]}.
Ik koos: {choices[comp_choice]}.\n
{win_message}
            ''') 
        except:
            pass
        finally:
            try_again = input('wil je stoppen: (y/N) ').strip().lower() == 'y'
            if try_again:
                break

def get_win_message(user_won):
    '''
        deze functie die geeft het bericht terug voor de uitslag van het potje.
        dit wordt gedaan door de varaibele userWon te vergelijken.
        als hij none is dan is het gelijk spel, is hij True dan heeft de speler 
        gewonen en anders heeft hij verloren
    '''
    if user_won == None:
        return 'Het is Gelijkspel.'
    elif user_won:
        return 'Jij wint!'
    else:
        return 'Ik win!'

def get_user_pick(choices):
        '''
            deze functie geeft de gebruiker de keuze uit de verschillende wapens.
            zodra de gebruiker deze invuld dan kijken we of hij in de lijst met 
            keuzes zit zoniet geven we een foutmelding en stoppen geven we False
            terug. zit hijn er wel in dan pakken we de index van de keuze in de 
            list met keuzes, deze gebruiken we namelijk om te kijken wie wint
        '''
        user_input = input(f'Kies je wapen [{", ".join(choices)}] > ').strip().lower()
        if not user_input in choices:
            print(f"Het wapen '{user_input}' is niet bekend")
            raise ValueError(user_input)

        # we voegen 1 toe aan de index voor het
        return choices.index(user_input)


def has_user_won(user_choice, comp_choice, total_choices=3):
    '''
        in deze functie kijken of de speler gewonnen heeft. als hij gewonnen heeft
        returnd de functie True, met gelijkspel None, en bij verlies False.
        we kijken op een uitgebroijde manier door te loopen voor een aantal keer
        dat wordt bepaald door het totaal aantal keuzes te delen door 2 en er 1 van 
        af te halen dus bij rps-101 is zijn er 50 wincondities per keuze en bij rps-255 zijn 1 
        daarvoor moeten ze wel in de goede winvolgorde staan.
    '''
    if user_choice == comp_choice:
        return None 

    for i in range((total_choices-1)/2):
        if (user_choice + i == comp_choice
         or user_choice == total_choices):
            return True 

    return False


if __name__ == '__main__':
    main()
