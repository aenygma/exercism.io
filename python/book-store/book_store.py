

DISCOUNT_TABLE = {1: 1.0, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}
COST_TABLE = {1: 8*1.0, 2: 8*2*0.95, 3: 8*3*0.9, 4: 8*4*0.8, 5: 8*5*0.75}

def cost(books):
    """ determine max discount for given books """

    # make a local copy before we mutate it
    local_books = books.copy()
    total_books = len(books)
    book_types = list(set(books))
    discount = DISCOUNT_TABLE.get(len(book_types), 0)
    # cost = bookprice * (books_without_discount + books_with_discount)
    cost = 8 * ((total_books - len(book_types)) + discount*len(book_types))
    return cost * 100

def calculate_total(books):

    if len(books) <= 5:
        return cost(books)
    return cost(books)

def make_groups(tbooks):

    ret = []
    books = tbooks.copy()

    while len(books) > 0:
        bset = list(set(books))
        [books.remove(i) for i in bset]
        ret.append(bset)
    return ret

#
# Note: 4 is the optimal number because
#   - a group of 5 doesn't offer a greater discount
#   - so, any extra over 4 would help bring other
#       groups to a higher discount bracker

def optimize(group1, group2):

    if not (((len(group1) > 4) and (len(group2) < 4)) or \
        ((len(group1) < 4) and (len(group2) > 4))):
        # already optimized
        return

