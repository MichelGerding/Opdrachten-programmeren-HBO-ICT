import math

def sq(x, power=2):
    """
        take x and raise it to the power of power
    """
    return x ** power

def interp(low, hi, fraction): 
    """
        get the fraction of a number between a low and a high 
    """
    return low + (hi - low) * float(fraction) 
def checkends(s):
    """
        Check if both ends are equal
    """
    return s[0] == s[-1]

def flipside(s):
    """
        pak de eerste helft en zet die voor aan een string. 
        als lengte oneven is is de eerste helft van s 1 korter 
    """
    str_len = len(s)
    if len(s) % 2 == 0:
        #even
        return s[int(str_len/2):] + s[:int(str_len/2)]
    else:
        #oneven
        return s[int(str_len/2-0.5):] + s[:int(str_len/2-0.5)]

def conver_from_seconds(seconds):
    """
        convert a number of seconds to a aount of days, hours, and seconds and return as list
    """
    intervals = [
        86400,    # 60 * 60 * 24
        3600,    # 60 * 60
        60,
        1,
    ]
    result = []

    for count in intervals:
        value = seconds // count
        seconds -= value * count
        result.append(value)

    return result 
