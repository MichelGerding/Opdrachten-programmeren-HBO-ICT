def mult(n,m):
    """mult returns the product of its two arguments. calculated by using recorsion

       Arguments: n and m are both integers
       Return value: the result of multiplying n and m
    """
    # return n + mult(n, m - 1)
    if m == 0:
        return 0
    elif m == 1:
        return n
    else:
        if m < 0:
            return n - mult(n, abs(m - 1))
        else:
            return n + mult(n, m - 1)

assert mult(6, 7) == 42
assert mult(6, -7) == -42
assert mult(-6, 7) == -42
assert mult(-6, -7) == 42
assert mult(6, 0) == 0
assert mult(0, 7) == 0
assert mult(0, 0) == 0

def dot(v1,v2):
    """ dot returns the dot product of 2 lists of equal length
        if the arrays are not equal in length or one is empty
        it returns 0.0. calculate it using recursion

        Arguments: v1 and v2 are both lists
        Return value: the dot product of v1 and v2 as float
    """
    if len(v1) == 0 or len(v2) == 0:
        return 0.0
    elif len(v1) != len(v2):
        return 0.0
    else:
        return v1[0]*v2[0] + dot(v1[1:], v2[1:])
    # if not len(v1) == len(v2):
    #     return 0.0
    # elif not len(v1) or not len(v2):
    #     return 0.0
    # else:
    #     return float(sum(x*y for x, y in zip(v1, v2)))

assert dot([5, 3], [6, 4]) == 42.0 
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6]) == 0.0
assert dot([], [6]) == 0.0
assert dot([], []) == 0.0


def ind(e, L):
    """ ind searches for the index of e in list L and returns it if it is found
        if it is not found it will return the length of L. look for the index using recursion

        Arguments: e a string or number, L a list or a string
        Return value: the index of e in L or the length of L
    """ 
    if len(L) == 0:
        return len(L)
    elif e == L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:])



assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100))) == 42
assert ind("hoi", ["hallo", 42, True]) == 3
assert ind("hoi", ["oh", "hoi", "daar"]) == 1
assert ind("i", "team") == 4
assert ind(" ", "nader onderzoek") == 5


def letter_score(let):
    """ letter_score takes a letter and returns the score of it in the game 
        scrabble using the dutch scoring system.
        if the letter is not a valid scrabble tile we will return 0

        Arguments: let is a string
        Return value: a intiger correspondig with the letters score 
    """ 
    
    if len(let) != 1:
        return 0
    if let in "adeinorst":
        return 1
    elif let in "ghl":
        return 2
    elif let in "bcmp":
        return 3
    elif let in "jkuvw":
        return 4
    elif let in "f":
        return 5
    elif let in 'z':
        return 6
    elif let in "xy":
        return 8
    elif let in "q":
        return 10
    return 0 



def scrabble_score(word):
    """ scrabble_score gives you the total amount of points for a word.
        the total amount of points is calculated recursively and utilizes
        the function letter_score

        Arguments: word a string
        Return value a integer with the value of the word 
    """
    if len(word) == 0:
        return 0
    else:
        return letter_score(word[0]) + scrabble_score(word[1:])


assert scrabble_score("quotums") == 24
assert scrabble_score("jacquet") == 24
assert scrabble_score("pyjama") == 20
assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 84
assert scrabble_score("?!@#$%^&*()") == 0
assert scrabble_score("") == 0


def transcribe(S):
    """ transcribe converts the certain letters to a different letter using 
        recursion and remove the letters not in the list to transcribe. 
        this function uses recursion

        Arguments: A string
        Return Value: the transcribed string
    """
    if len(S) == 0:
        return ''
    elif S[0] == 'A':
        return 'U' + transcribe(S[1:])
    elif S[0] == 'C':
        return 'G' + transcribe(S[1:])
    elif S[0] == 'G':
        return 'C' + transcribe(S[1:])
    elif S[0] == 'T':
        return 'A' + transcribe(S[1:])
    else:
        return '' + transcribe(S[1:])

assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'  # De spatie verdwijnt
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('hanze')    == ''         # Andere tekens verdwijnen
assert transcribe('')         == ''

#
# Ik heb alle STRING-opgaven van CodingBat gemaakt.
#


#
# Ik heb alle STRING-opgaven van CodingBat gemaakt.
#
#
# Ik heb alle LIJST-opgaven van CodingBat gemaakt.
#
def get_consonants(s):
    """get all consonants using recursion
    """
    if len(s) == 0:
        return ''
    elif not s[0] in 'bcdfghjklmnpqrstvxyz':
        # return get_consonants(s[1:])
        return ''
    else:
        return s[0] + get_consonants(s[1:])

def pig_latin(word):
    """ pig_latin takes a word and returns the pig latin version of it

        Arguments: word a string
        Return value: a string with the pig latin version of the word
    """
    word = word.strip().lower()
    medeklinkers = 'bcdfghjklmnpqrstvxyz' 
    klinkers = 'aeiou'

    if (len(word) == 0):
        return ''
    
    if word[0] in klinkers:
        return word + 'hee'
    elif word[0] == 'y' and word[1] in medeklinkers:
            return word + 'hee'
    elif word[0] in medeklinkers:
        
        # convert to use recursive function
        consonants = get_consonants(word)
        pig_latin = word[len(consonants):] + f'{consonants}ee'
        return pig_latin
    
    return '' 

# tests for pig_latin
assert pig_latin('straat') == 'aatstree'
assert pig_latin('ypsilon') == 'ypsilonhee'
assert pig_latin('yoghurt') == 'oghurtyee'