# Programmeren I, Practicum 4
# Bestandsnaam: wk4ex1.py
# Naam:
# Probleemomschrijving: Geluidsbewerking

import random
import math
from audio import *


# een functie zodat we kunnen beginnen met een opfrisser
# over list comprehensions...
def three_ize(L):
    """three_ize is a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # dit is een voorbeeld van een list comprehension
    lc = [3 * x for x in L]
    return lc


# Te schrijven functie #1: scale
def scale(L, scale_factor):
    """ scale is a function that accepts a list and a float
        and returns a scaled list of elements

        Arguments: L, a list of numbers
                  scale_factor, a number to multiply every entry of L by
        Return Values: A list of numbers
    """
    return [x * scale_factor for x in L]

#
# Tests for scale
#
assert scale([70, 80, 420], 0.1) == [7.0, 8.0, 42.0]
assert scale([70, 80, 420], 0.5) == [35.0, 40.0, 210.0]
assert scale([70, 80, 420], 1.0) == [70.0, 80.0, 420.0]
assert scale([70, 80, 420], 2.0) == [140.0, 160.0, 840.0]

# hier is een voorbeeld van hoe je op een andere
# manier de functie three_ize kan schrijven:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # nog een voorbeeld van een list comprehension
    n = len(L)
    lc = [3 * L[i] for i in range(n)]
    return lc

# Te schrijven functie #2: add_2
def add_2(L, m):
    """ add_2 adds 2 lists to each other by using the index to loop
        over the lists. if one list is shorter then the other it will
        return when the shortest list runs out of elements

        Return Value: a list of numbers
    """
    n = min(len(L), len(m))
    return [L[i] + m[i] for i in range(n)]

#
# Tests for add_2
#
assert add_2([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert add_2([1, 2, 3], [4, 5, 6, 7]) == [5, 7, 9]
assert add_2([1, 2, 3], [4, 5, 6, 7, 8]) == [5, 7, 9]
assert add_2([1, 2, 3, 4], [5, 6, 7, 8]) == [6, 8, 10, 12]

# Te schrijven functie #3: add_3
def add_3(L,m, p):
    """ add_3 adds 3 lists to each other by using the index to loop
        over the lists. if one list is shorter then the other it will
        return when the shortest list runs out of elements

        Return Value: a list of numbers
    """
    n = min(len(L), len(m), len(p))
    return [L[i] + m[i] + p[i] for i in range(n)]
#
# test for add_3
#
assert add_3([1, 2, 3], [4, 5, 6], [7, 8, 9]) == [12, 15, 18]
assert add_3([1, 2, 3], [4, 5, 6, 7], [7, 8, 9]) == [12, 15, 18]
assert add_3([1, 2, 3], [4, 5, 6, 7, 8], [7, 8, 9]) == [12, 15, 18]
assert add_3([1, 2, 3, 4], [5, 6, 7, 8], [7, 8, 9]) == [13, 16, 19]

# Te schrijven functie #4: add_scale_2
def add_scale_2(L, m, L_scale, m_scale):
    """ add_sacle_2 adds 2 lists after scaling it by the corrisponding scale
        this function returns the same amount of elements of the shortest 
        of the 2 lists

        Arguments:  l, lists of numbers
                    m, lists of numbers
                    L_scale, A number to scale the corresponding list by
                    m_scale, A number to scale the corresponding list by
        Return value: a list with the scaled and added values
    """

    n = min(len(L), len(m))  
    L_scaled = scale(L, L_scale)
    m_scaled = scale(m, m_scale)
    return [L_scaled[i] + m_scaled[i] for i in range(n)]

#
# Tests for add_scale_2
#
assert add_scale_2([1, 2, 3], [4, 5, 6], 1, 1) == [5, 7, 9]
assert add_scale_2([1, 2, 3], [4, 5, 6, 7], 1, 1) == [5, 7, 9]
assert add_scale_2([1, 2, 3, 4], [5, 6, 7, 8], 0.5, 0.5) == [3, 4, 5, 6]
assert add_scale_2([10, 20, 30], [7, 8, 9], 0.1, 10) == [71.0, 82.0, 93.0]
assert add_scale_2([10, 20, 30], [7, 8], 0.1, 10) == [71.0, 82.0]
# Hulpfunctie: randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x


# Te schrijven functie #5: replace_some
def replace_some(L, chance_of_replacing):
    return [randomize(i, chance_of_replacing) for i in L]

#
# Tests for replace_some
#
assert replace_some(range(40, 50), 0) == list(range(40, 50))
assert replace_some([42], 1.0) != [42]

# de functies hieronder betreffen geluidsbewerking...
#
#


# een functie om te zorgen dat alles werkt
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# De voorbeeldfunctie change_speed
def change_speed(filename, newsr):
    """change_speed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Het originele geluid afspelen...")
    play(filename)

    sound_data = [0, 0]             # een "lege" lijst
    read_wav(filename, sound_data)  # laad gegevens IN sound_data

    samps = sound_data[0]           # de samples van de ruwe geluidsgolven

    print("De eerste 10 geluidsdruksamples zijn\n", samps[:10])
    sr = sound_data[1]              # de sampling rate, sr

    print("Het aantal samples per seconde is", sr)

    # deze regel is niet echt nodig, maar staat hier voor de consistentie...
    newsamps = samps                      # dezelfde samples als eerder
    new_sound_data = [newsamps, newsr]    # nieuwe geluidsgegevens
    write_wav(new_sound_data, "out.wav")  # sla de gegevens op naar out.wav
    print("\nNieuw geluid afspelen...")
    play('out.wav')   # speel het nieuwe bestand 'out.wav' af


def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Het originele geluid afspelen...")
    play(filename)

    print("Geluidsgegevens inlezen...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Nieuw geluid berekenen...")
    # dit bepaalt het middelpunt en noemt dat x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #1: reverse
def reverse(filename):
    """ Reverse takes in a filename and plays a the soundfile in reverse  
        Arguments: filename, A string containing the path to a .wav file
    """
    print('Geluidsgegevens inlezen...')
    sound_data = [0,0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print('Nieuw geluid berekenen...')
    newsamps = samps[::-1]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print('De nieuwe geluids opslaan...')
    write_wav(new_sound_data, "out.wav")

    print('Nieuw geluid afspelen...')
    play('out.wav')

# reverse("swfaith.wav")
# Te schrijven geluidsfunctie #2: volume
def volume(filename, scale_factor):
    """ volume takes in the path to a soundfile and amplifies the volume by
        scale factor. after it has done that the sound will be played and saved
        to a file called out.wav

        Arguments:  filename, a string containing a path to a .wav file
                    scale_factor, a number to scale the volume by
    """
    print('Geluidsgegevens inlezen...')
    sound_data = [0,0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print('Nieuw geluid berekenen...')
    newsamps = scale(samps, scale_factor)
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print('De nieuwe geluids opslaan...')
    write_wav(new_sound_data, "out.wav")

    print('Nieuw geluid afspelen...')
    play('out.wav')

# volume("swfaith.wav", .5)
# Te schrijven geluidsfunctie #3: static
def static(filename, probability_of_static):
    """ static is a function that takes a path to a audio file
        and plays it with added static

        Arguments:  filename, a string containing a path to a .wav file
                    probability_of_static, a float with the change of static
    """
    print('Geluidsgegevens inlezen...')
    sound_data = [0,0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print('Nieuw geluid berekenen...')
    newsamps = replace_some(samps, probability_of_static)
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print('De nieuwe geluids opslaan...')
    write_wav(new_sound_data, "out.wav")

    print('Nieuw geluid afspelen...')
    play('out.wav')

# static("swfaith.wav", .05)
# Te schrijven geluidsfunctie #4: overlay
def overlay(
    filename1, 
    filename2, 
    file1_volume=1, 
    file2_volume=1, 
    extend_shortest=False,
    repeat = True):
    """ overlay is a function that takes in 2 filepaths and
        overlays the 2 soundfiles. by default it takes the length of the 
        shortest soundfile, and then plays it. 

        Arguments:  filename, a string containing a path to a .wav file
                    filename, a string containing a path to a .wav file
                    file1_volume, a number to scale the volume to
                    file2_volume, a number to scale the volume to
                    extend_shortest, A boolean that defines if the longer
                                    soundfile gets cut of or not
    """
    print('Geluidsgegevens bestand 1 inlezen...')
    sound_data_1 = [0,0]
    read_wav(filename1, sound_data_1)
    samps_1 = sound_data_1[0]
    sr = sound_data_1[1]

    print('Geluidsgegevens bestand 2 inlezen...')
    sound_data_2 = [0,0]
    read_wav(filename2, sound_data_2)
    samps_2 = sound_data_2[0]
    
    print('Nieuw geluid berekenen...')
    if extend_shortest:
        if len(samps_1) > len(samps_2):
            short_len = len(samps_2)
            short_sample = samps_2
            long_len = len(samps_1)
        else: 
            short_len = len(samps_1)
            short_sample = samps_1
            long_len = len(samps_2)

        # extend sample
        if repeat:
            len_difference = long_len - short_len
            while len_difference > 0:
                short_sample += short_sample[len_difference:]
                    
                len_difference -= short_len
        else:
            short_sample.extend([0] * (len(long_len) - len(short_len)))

        if long_len == len(samps_1):
            samps_2 = short_sample
        else:
            samps_1 = short_sample


    newsamps = add_scale_2(samps_1, samps_2, file1_volume, file2_volume) 
    new_sound_data = [newsamps, sr]

    print('De nieuwe geluids opslaan...')
    write_wav(new_sound_data, "out.wav")

    print('Nieuw geluid afspelen...')
    play('out.wav')



# overlay("swfaith.wav", "swnotry.wav", 0,1,0,1 )

# Te schrijven geluidsfunctie #5: echo
def echo(filename, time_delay):
    """ The function echo adds a echo of time_delay in seconds
    """

    print('Geluidsgegevens inlezen...')
    sound_data = [0,0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print('Nieuw geluid berekenen...')
    samples_delay = int(sr*time_delay)
    samps_2 = [0]*samples_delay + samps
    newsamps = add_scale_2(samps, samps_2, 1, 1)
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print('De nieuwe geluids opslaan...')
    write_wav(new_sound_data, "out.wav")

    print('Nieuw geluid afspelen...')
    play('out.wav')

# echo("swfaith.wav", .1)


# Hulpfunctie om pure tonen te genereren
def gen_pure_tone(freq, seconds, sound_data):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    if sound_data != [0, 0]:
        print("De waarde van sound_data moet [0, 0] zijn.")
        return
    sampling_rate = 22050
    # hoeveel samples we moeten genereren
    nsamples = int(seconds*sampling_rate)  # naar beneden afgerond
    # de factor f om de frequentie te schalen
    f = 2*math.pi/sampling_rate   # omrekenen van samples naar Hz
    # de factor a om de amplitude te schalen
    a = 32767.0
    sound_data[0] = [a * math.sin(f*n*freq) for n in range(nsamples)]
    sound_data[1] = sampling_rate
    return sound_data


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Toon genereren...")
    sound_data = [0, 0]
    gen_pure_tone(freq, time_in_seconds, sound_data)

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #6: chord
def chord(f1,f2,f3, time_in_seconds):
    """ generate a chord by using 3 frequenties for a certain duration
    """

    samps1, sr1 = gen_pure_tone(f1, time_in_seconds, [0, 0])
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds, [0, 0])
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds, [0, 0])

    newsamps = add_3(samps1, samps2, samps3)

    new_sound_data = [newsamps, sr1]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play("out.wav")

chord(440.000, 523.251, 659.255, 1.0)