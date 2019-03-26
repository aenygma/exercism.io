
BASE = "On the %s day of Christmas my true love gave to me: "
#SONG = ["twelve Drummers Drumming, ",
#        "eleven Pipers Piping, ",
#        "ten Lords-a-Leaping, ",
#        "nine Ladies Dancing, ",
#        "eight Maids-a-Milking, ",
#        "seven Swans-a-Swimming, ",
#        "six Geese-a-Laying, ",
#        "five Gold Rings, ",
#        "four Calling Birds, ",
#        "three French Hens, ",
#        "two Turtle Doves, ",
#        "and a Partridge in a Pear Tree."]
SONG = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves,",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,"]

ORDINALS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
    'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

def recite(start_verse, end_verse):
    base = (BASE % ORDINALS[start_verse-1])
    lines = " ".join(SONG[1:start_verse][::-1])
    lines += SONG[0] if start_verse == 1 else " and " + SONG[0]
    return [base + lines]


