def raindrops(number):
    """ return appropriate string"""

    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'}
    ret = ""

    # apply the text map
    for (div, text) in sounds.items():
        if number%div == 0:
            ret += text

    # if none found, return number
    if ret == "":
        ret = str(number)

    return ret
