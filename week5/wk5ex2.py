def num_to_base_b(n, b):
    """
        convert the number n in base10 to base b using recursion 
        and return it as a string. if n is o return a empty string
    """
    if n == 0:
        return ''
    else:
        return num_to_base_b(n // b, b) + str(n % b)

assert num_to_base_b(3116, 9) == '4242'
assert num_to_base_b(141474, 8) == '424242'
assert num_to_base_b(42, 8) == '52'
assert num_to_base_b(42, 5) == '132'
assert num_to_base_b(42, 10) == '42'
assert num_to_base_b(42, 2) == '101010'
assert num_to_base_b(4, 2) == '100'
assert num_to_base_b(4, 3) == '11'
assert num_to_base_b(4, 4) == '10'
assert num_to_base_b(0, 4) == ''
assert num_to_base_b(0, 2) == ''

def base_b_to_num(s,b):
    """
        Convert string s in base b to bae 10 and return it
    """
    if s == '':
        return 0
    else:
        return b * base_b_to_num(s[:-1], b) + int(s[-1])

assert base_b_to_num("5733", 9) == 4242
assert base_b_to_num("1474462", 8) == 424242
assert base_b_to_num("222", 4) == 42
assert base_b_to_num("101010", 2) == 42
assert base_b_to_num("101010", 3) == 273
assert base_b_to_num("101010", 10) == 101010
assert base_b_to_num("11", 2) == 3
assert base_b_to_num("11", 3) == 4
assert base_b_to_num("11", 10) == 11
assert base_b_to_num("", 10) == 0 

def base_to_base(b1, b2, s_in_b1):
    """
        convert string s_in_b1 in base b1 to base 10 and then convert 
        it to base b2 and return it 
    """ 
    return num_to_base_b(base_b_to_num(s_in_b1, b1), b2)


assert base_to_base(2, 10, "11")== '3'
assert base_to_base(10, 2, "3") == '11'
assert base_to_base(3, 5, "11") == '4'
assert base_to_base(2, 3, "101010")== '1120'
assert base_to_base(2, 4, "101010")== '222'
assert base_to_base(2, 10, "101010")== '42'
assert base_to_base(5, 2, "4321")== '1001001010'
assert base_to_base(2, 5, "1001001010")== '4321'


def add(s, t):
    """
        The function add converts variables s and t to base 10 add 
        them together and then returns them as a binary string
    """
    if s == '':
        return t
    elif t == '':
        return s
    else:
        return num_to_base_b(base_b_to_num(s,2) + base_b_to_num(t,2), 2)


assert add("11", "1") == '100'
assert add("11", "100") == '111'
assert add("110", "11") == '1001'
assert add("11100", "11110") == '111010'
assert add("10101", "10101") == '101010'


def add_b(x, y):
    """
        the function add_b adds the binary strings s and t together. without converting them to base10
        by using addtition and a carry bit.
    """
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    obj = ['',0]
    [add_b_helper(obj, x, y, i) for i in range(max_len - 1, -1, -1)]
    if obj[1] !=0 : obj[0] = '1' + obj[0]
    return obj[0].zfill(max_len)

def add_b_helper(obj, x,y,i):
    """
        add 2 bits and calculate carry. how does it work? i have no idea. some pass by reference shit
    """
    obj[0] = ('1' if (obj[1] + (1 if x[i] == '1' else 0) + (1 if y[i] == '1' else 0)) % 2 == 1 else '0') + obj[0]
    obj[1] = 0 if (obj[1] + (1 if x[i] == '1' else 0) + (1 if y[i] == '1' else 0)) < 2 else 1

assert add_b("11", "1") == '100'
assert add_b("11", "100") == '111'
assert add_b("110", "11") == '1001'
assert add_b("11100", "11110") == '111010'
assert add_b("10101", "10101") == '101010'
assert add_b("10101", "10101") == '101010'

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


def compress(s):
    """
        compress a string of 1's and 0's using run time encoding nd recursion 
    """

    if s == '':
        return ''
    
    output = ''
    # loop for all chars
    count = 1
    lastChar = s[0]
    for c in s[1:]:
        if c == lastChar:
            count += 1
        else:
            # make a byte with
            output += str(lastChar) + bin(count)[2:].zfill(7)
            count = 1
            lastChar = c
    
    output += str(lastChar) + bin(count)[2:].zfill(7)
    return output

def uncompress(s):
    return ''.join([s[i*8: (i+1)*8][0] * int(s[i*8: (i+1)*8][1:], 2) for i in range(len(s) // 8)])


for i in range(64**2):
    assert uncompress(compress(str(i))) == str(i)
