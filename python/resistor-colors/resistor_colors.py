RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green",
    "blue", "violet", "grey", "white"]

def value(colors):
    vals = [RESISTOR_COLORS.index(color) for color in colors]
    return vals[0]*10 + vals[1]
