import random
from typing import List
from collections import Counter

def encipher(s, n) -> str:
    """encipher a string by rotating its letters n to the right in the alphabet

        Arguments:  s, the string to encode
                    n, the amount of times we want to ratate it
        Return Value: The enciphered string
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_string = ""

    # for char in s:
        # if char in alphabet:
        #     new_string += alphabet[(alphabet.index(char) + n) % 26]
        # elif char in upper_alphabet:
        #     new_string += upper_alphabet[(upper_alphabet.index(char) + n) % 26] 
        # else:
        #     new_string += char
    if len(s) == 0:
        return ''
    elif s[0] in alphabet:
        return alphabet[(alphabet.index(s[0]) + n) % 26] + encipher(s[1:], n)
    elif s[0] in upper_alphabet:
        return upper_alphabet[(upper_alphabet.index(s[0]) + n) % 26] + encipher(s[1:], n)
    else:
        return s[0] + encipher(s[1:], n)


assert encipher("xyza", 1) == "yzab"
assert encipher("Z A", 1) == "A B" 
assert encipher('*ab?', 1) == '*bc?' 
assert encipher('Dit is een string!', 1) == 'Eju jt ffo tusjoh!' 
assert encipher('Caesarcijfer? Ik heb liever Caesarsalade.', 25) == 'Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.' 

def decipher(s):
    """ the function decipher tries to decipher a string enciphered by 
        the function encipher. the function does this by calculating 
        the centence with the letters that have the highest change of 
        being in the ducth language.
    """ 

    deciphered_strings = [encipher(s, i) for i in range(26)]
    scores = [string_score(string) for string in deciphered_strings]
    max_score_index = scores.index(max(scores))

    return deciphered_strings[max_score_index]

def string_score(s):
    if len(s) == 0:
        return 0
    return letter_prob(s[0]) + string_score(s[1:])

def letter_prob(c):
    """If c is an alphabetic character,
       we return its monogram probability (for Dutch),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       https://www.sttmedia.com/characterfrequency-nederlands
    """
    if c == 'e' or c == 'E':
        return 0.1909
    if c == 'n' or c == 'N':
        return 0.0991
    if c == 'a' or c == 'A':
        return 0.0769
    if c == 't' or c == 'T':
        return 0.0642
    if c == 'i' or c == 'I':
        return 0.0630
    if c == 'o' or c == 'O':
        return 0.0581
    if c == 'r' or c == 'R':
        return 0.0562
    if c == 'd' or c == 'D':
        return 0.0541
    if c == 's' or c == 'S':
        return 0.0384
    if c == 'l' or c == 'L':
        return 0.0380
    if c == 'h' or c == 'H':
        return 0.0312
    if c == 'g' or c == 'G':
        return 0.0312
    if c == 'k' or c == 'K':
        return 0.0279
    if c == 'm' or c == 'M':
        return 0.0256
    if c == 'v' or c == 'V':
        return 0.0224
    if c == 'u' or c == 'U':
        return 0.0212
    if c == 'j' or c == 'J':
        return 0.0182
    if c == 'w' or c == 'W':
        return 0.0172
    if c == 'z' or c == 'Z':
        return 0.0160
    if c == 'p' or c == 'P':
        return 0.0149
    if c == 'b' or c == 'B':
        return 0.0136
    if c == 'c' or c == 'C':
        return 0.0130
    if c == 'f' or c == 'F':
        return 0.0073
    if c == 'y' or c == 'Y':
        return 0.0006
    if c == 'x' or c == 'X':
        return 0.0005
    if c == 'q' or c == 'Q':
        return 0.0001
    return 1.0


assert decipher('Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.') == 'Caesarcijfer? Ik heb liever Caesarsalade.'
assert decipher( 'Aadxas ue exqotfe pq haadflqffuzs hmz baxufuqw yqf mzpqdq yuppqxqz.')== 'Oorlog is slechts de voortzetting van politiek met andere middelen.'
assert decipher('Lvkeg lvyon') == 'Eodxz eorhg'

def blsort(L):
    """ Sort a list with binary values by getting the amount of 0's and 1's
    """

    count_of_0s = L.count(0)
    count_of_1s = len(L)-count_of_0s
    return gen_b_list(count_of_0s, count_of_1s)

def gen_b_list(amount_0, amount_1):
    """generate a list with a set amount of 0's and 1's"""
    return [0]*amount_0 + [1]*amount_1

def shuffle(b_list):
    shuffled_list = b_list
    random.shuffle(shuffled_list)
    return shuffled_list

assert blsort(shuffle(gen_b_list(100,2))) == gen_b_list(100,2)
assert blsort(shuffle(gen_b_list(100,0))) == gen_b_list(100,0)
assert blsort(shuffle(gen_b_list(0,100))) == gen_b_list(0,100)
assert blsort(shuffle(gen_b_list(100,100))) == gen_b_list(100,100)
assert blsort(shuffle(gen_b_list(100,10))) == gen_b_list(100,10)


 
# def partition(arr, low, high):
#     i = (low-1)
#     pivot = arr[high]


#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]
  
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1)
  
  
def gensort(arr) -> List:
    """ gensort sorts a list of numbers only using list comprehension and recursion

        Arguments:  arr, A list of numbers to be sorted
        Return value: a sorted list  
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return gensort(less) + [pivot] + gensort(greater)
   
assert gensort([42, 1, 3.14]) == [1, 3.14, 42]
assert gensort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert gensort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert gensort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert gensort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def lingo(s, t):
    """ calculates the lingo score of two strings

        Arguments:  s, The first string
                    t, The second string
        Return value: the lingo score
    """

    letters = Counter(s) & Counter(t)
    return sum(letters.values())


assert lingo('diner', 'proza')  ==  1
assert lingo('beeft', 'euvel')  ==  2
assert lingo('gattaca', 'aggtccaggcgc') ==  5
assert lingo('gattaca', '') ==  0
assert lingo('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz') == 26

def exact_change(target, L):
    """ the function exact_change checks if the numbers in the list 
        have a combination equal to target
    """
    if target == 0:
        return True
    if L == []:
        return False
    if L[0] > target:
        return exact_change(target, L[1:])
    return exact_change(target-L[0], L[1:]) or exact_change(target, L[1:])

assert exact_change(42, [25, 1, 25, 10, 5, 1]) == True
assert exact_change(42, [25, 1, 25, 10, 5]) == False
assert exact_change(42, [23, 1, 23, 100]) == False
assert exact_change(42, [23, 17, 2, 100]) == True
assert exact_change(42, [25, 16, 2, 15]) == True

def lcs(s,t):
    """ the function lcs gets the longest common subsequence of 2 strings

        Arguments:  s, The first string
                    t, The second string
        Return value: the longest common subsequence
    """
    if s == '' or t == '':
        return ''
    if s[0] == t[0]:
        return s[0] + lcs(s[1:], t[1:])
    return max(lcs(s[1:], t), lcs(s, t[1:]), key=len)

assert lcs('mens', 'chimpansee') == 'mns'
assert lcs('gattaca', 'tacgaacta') == 'gaaca'
assert lcs('wow', 'wauw') == 'ww'
assert lcs('', 'wauw') == ''
assert lcs('abcdefgh', 'efghabcd') == 'efgh'

def make_change(target, L):
    """ the function make_change returns which coins out of list L 
        to use to count up to the target. if there are no possible 
        combinations it will return false, if there is it will return 
        an array
    """
    if target == 0:
        return []
    if L == []:
        return False
    if L[0] > target:
        return make_change(target, L[1:])
    use_it = make_change(target-L[0], L[1:])
    if use_it == False:
        return make_change(target, L[1:])
    else:
        return [L[0]] + use_it

assert sorted(make_change(42, [25, 1, 25, 10, 5, 1])) == [1, 1, 5, 10, 25]
assert make_change(42, [23, 1, 23, 100]) == False
assert sorted(make_change(42, [23, 17, 2, 100])) == [2, 17, 23]
assert make_change(0, [4, 5, 6]) == []
assert make_change(-47, [4, 5, 6]) == False
assert make_change(0, []) == []