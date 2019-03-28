from string import ascii_uppercase

def make_diamond(letter):
    """ given a letter, make a diamond with it """

    val = ascii_uppercase.index(letter) + 1
    ret = [None]*(val+val-1)

    for i in range(val):
        ent = ascii_uppercase[i]
        ent = ent.rjust(val-i+len(ent)-1)
        ent = ent.ljust(i+len(ent))
        # reflect on y-axis
        rent = ent[::-1][1:]
        ret[i] = ent + rent
        # reflect on x-axis
        ret[len(ret)-i-1] = ent + rent
    return "\n".join(ret) + "\n"
