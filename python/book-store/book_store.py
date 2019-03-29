class Chunk(object):
    """
    given a list of items, chunk them in unique groups
    """

    def __init__(self, tlist):
        self.tlist = tlist.copy()

    @property
    def counts(self):
        """  return a tally of counts"""

        ret = []
        for i in set(self.tlist):
            ret.append((i, self.tlist.count(i)))

        # sort by counts
        ret.sort(key=lambda x: x[1], reverse=True)
        return ret

    def get_uniq_n(self, num=4):
        """ return n number of uniq items """

        ret = []
        tmp = []
        idx = 0

        # iterate list, or until 4 items grabbed
        #while (idx < len(self.counts)) and (len(tmp) < num):

        while True:
            print("> x:", idx, tmp, ret)

            # done with group, next group
            if len(tmp) >= num:
                ret.append(tmp)
                tmp = []
                idx = 0

            # we're done with entire list
            if idx >= len(self.counts):
                ret.append(tmp)
                tmp = []
                idx = 0

            # return
            if not self.tlist:
                return ret

            val, _ = self.counts[idx]
            if val not in tmp:
                idx = 0
                tmp.append(val)
                self.tlist.remove(val)
            else:
                idx += 1

    def __repr__(self):
        return repr(self.tlist)

    get_groups = get_uniq_n

DISCOUNT_TABLE = {1: 1.0, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}

def cost(books):
    """ return cost for a set of books """

    num_types = len(set(books))
    assert num_types < 6, "Discounts indeterminate"
    return DISCOUNT_TABLE.get(num_types, 0) * 8 * len(books) * 100

def calculate_total(books):
    """ return minimum cost for all books, per the discounts """

    if len(books) <= 5:
        return cost(books)

    # try 4-group chunks
    cost4 = sum(map(cost, Chunk(books).get_groups(4)))

    # try 5-group chunks
    cost5 = sum(map(cost, Chunk(books).get_groups(5)))

    # return whatever's smaller
    return min(cost4, cost5)
