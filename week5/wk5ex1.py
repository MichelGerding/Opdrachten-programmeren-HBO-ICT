# Programmeren I, Practicum 5
# Bestandsnaam: wk5ex1
# Naam: Michel Gerding
# Probleemomschrijving: conversie binair <-> decimaal

def is_odd(n):
    """
        The function is_odd returns a boolean of True if the input is 
        a odd number. This is calculated by taking the remainder of n/2 
        and checking if it is 0 by inverting the boolean value(0 == False)
    """
    return bool(n%2)

assert not is_odd(42)
assert is_odd(43)

def num_to_binary(n):
    """
        The function num_to_binary converts the number n to a binary string 
        and returns it.
        it calculates it using recursion
    """
    if n == 0:
        return ''
    elif n == 1:
        return '1'
    else:
        return num_to_binary(n//2) + str(n%2)

assert num_to_binary(0) == '', num_to_binary(0)
assert num_to_binary(1) == '1'
assert num_to_binary(4) == '100'
assert num_to_binary(10) == '1010'
assert num_to_binary(42) == '101010'
assert num_to_binary(100) == '1100100'


def binary_to_num(s):
    """
        the function binary_to_num converts a string of bits to a 
        intiger with the use of recursion
    """
    if s == '':
        return 0
    else:
        return binary_to_num(s[:-1])*2 + int(s[-1])

assert binary_to_num("100") == 4
assert binary_to_num("1011") == 11
assert binary_to_num("00001011") == 11
assert binary_to_num("") == 0
assert binary_to_num("0") == 0
assert binary_to_num("1100100") == 100
assert binary_to_num("101010") == 42


def increment(s):
    """
        The function increment increments a binary string and returns it with 
        padding of value 0. it converst it by using the functions
        num_to_binary and binary_to_num
    """

    len_of_s = len(s)
    if s == '1'*len_of_s:
        return '0'*len_of_s
    else:
        incremented_s = num_to_binary(binary_to_num(s) + 1)
        return '0'*(len_of_s - len(incremented_s)) + incremented_s 

assert increment("00000000") == '00000001'
assert increment("00000001") == '00000010'
assert increment("11111111") == '00000000'
assert increment("10101010") == '10101011'
assert increment("10101011") == '10101100'

def count(s,n):
    """
        the function count increments the binary string s n times and prints every 
        version of it. after it is done incrementing it we will return the value
    """

    print(s)
    if n <= 0:
        return s
    else:
        return count(increment(s), n-1)

# assert count("00000000", 3) == "00000011"
# assert count("00000000", 4) == "00000100"
# assert count("11111110", 5) == "00000011"
# assert count("10101010", 3) == "10101101"

def num_to_ternary(n):
    """
        convert n to a ternary number using recursion
    """
    if n == 0:
        return ''
    elif n == 1:
        return '1'
    else:
        return num_to_ternary(n//3) + str(n%3)

assert num_to_ternary(0) == ''
assert num_to_ternary(42) == '1120'
assert num_to_ternary(421) == '120121'
assert num_to_ternary(4242) == '12211010'
assert num_to_ternary(42421) == '2011012011'

def ternary_to_num(s):
    """
        convert a ternary number to a intiger
    """
    if s == '':
        return 0
    else:
        return ternary_to_num(s[:-1])*3 + int(s[-1])


assert ternary_to_num("1120") == 42
assert ternary_to_num("12211010") == 4242
assert ternary_to_num("2011012011") == 42421
assert ternary_to_num("") == 0
assert ternary_to_num("0") == 0
assert ternary_to_num("1101") == 37
assert ternary_to_num("101") == 10
assert ternary_to_num("100") == 9


def balanced_ternary_to_num(s):
    """
        convert a balanced ternary to a base 10 intiger. 
        A balanced ternary exists of +,- and 0. a + stands for 1, 
        a - for -1 and a 0 for 0  
    """
    return sum([('-0+'.index(s[-i-1])-1)*(3**i) for i in range(len(s)) if s[-i-1] in '-0+'])

assert balanced_ternary_to_num("+---0") == 42
assert balanced_ternary_to_num("++-0+") == 100
assert balanced_ternary_to_num("-0+") == -8
assert balanced_ternary_to_num("+") == 1
assert balanced_ternary_to_num("-") == -1
assert balanced_ternary_to_num("0") == 0
assert balanced_ternary_to_num("") == 0


def num_to_balanced_ternary(n):
    """
        convert a number to a balanced ternary without using loops 
    """

    if n == 0:
        return ''
    n, rem = divmod(n, 3)

    if rem == 2:
        rem  = -1
        n+= 1
    
    if rem == 0:
        return num_to_balanced_ternary(n) + '0'
    else: 
        if rem == 1:
            return num_to_balanced_ternary(n) +'+'
        else:
            return num_to_balanced_ternary(n) + '-'


assert num_to_balanced_ternary(42) == '+---0'
assert num_to_balanced_ternary(100) == '++-0+'
assert num_to_balanced_ternary(-8) == '-0+'
assert num_to_balanced_ternary(0) == ''
