GRID_NUMBERS = {
    '0': [
        " _ ",
        "| |",
        "|_|",
        "   "],
    '1': [
        "   ",
        "  |",
        "  |",
        "   "],
    '2': [
        " _ ",
        " _|",
        "|_ ",
        "   "],
    '3':[
        " _ ",
        " _|",
        " _|",
        "   "],
    '4':[
        "   ",
        "|_|",
        "  |",
        "   "],
    '5':[
        " _ ",
        "|_ ",
        " _|",
        "   "],
    '6':[
        " _ ",
        "|_ ",
        "|_|",
        "   "],
    '7':[
        " _ ",
        "  |",
        "  |",
        "   "],
    '8':[
        " _ ",
        "|_|",
        "|_|",
        "   "],
    '9':[
        " _ ",
        "|_|",
        " _|",
        "   "]
}
UNKNOWN_CHAR = '?'

def convert(grid):
    """ given an ocr grid, covert them to numerals """

    # validate grid rows
    if len(grid)%4:
        raise ValueError("Improper grid rows")

    # validate column lengths
    lengths = list(set(map(len, grid)))
    if len(lengths) > 1:
        raise ValueError("Inconsistent column lengths")
    elif lengths[0]%3:
        raise ValueError("Improper grid columns")

    ret = []
    for ridx in range(0, len(grid), 4):
        translated_row = ""
        for cidx in range(0, len(grid[ridx]), 3):
            elem = [x[cidx: cidx+3] for x in grid[ridx: ridx+4]]
            translated_row += lookup_number(elem)

        ret.append(translated_row)
    return ",".join(ret)

def lookup_number(input_grid):
    """ lookup a number in the grid"""

    for (val, grid_number) in GRID_NUMBERS.items():
        if input_grid == grid_number:
            return val
    return UNKNOWN_CHAR
