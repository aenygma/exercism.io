class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass

class Element:
    """ element of the circular buffer """

    def __init__(self):
        self._value = None
        self.empty = True

    @property
    def value(self):
        """ read from cell """

        if self.empty:
            raise BufferEmptyException("Reading from empty space")
        self.empty = True
        return self._value

    @value.setter
    def value(self, val):
        """ write to cell """

        if not self.empty:
            raise BufferFullException("Writing to occupied space")
        self._value = val
        self.empty = False

    @value.deleter
    def value(self):
        """ clear a cell """

        self._value = None
        self.empty = True

    def __repr__(self):
        return f"<v: {self._value}, e: {self.empty}>"

class CircularBuffer(object):
    """ implement a circular buffer """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [Element() for _ in range(capacity)]
        self.ridx = 0
        self.widx = 0

    def _incr(self):
        self.ridx = (self.ridx + 1) % self.capacity

    def _incw(self):
        self.widx = (self.widx + 1) % self.capacity

    def read(self):
        """ read from current location """

        val = self.data[self.ridx].value
        self._incr()
        return val

    def write(self, data):
        """ write to current location """

        self.data[self.widx].value = data
        self._incw()

    def overwrite(self, data):
        """ sudo write to location """

        del(self.data[self.widx].value)
        self.data[self.widx].value = data
        # if we're rewriting current read, nudge it over.
        if self.ridx == self.widx:
            self._incr()
        self._incw()

    def clear(self):
        """ clear buffer """

        for i in self.data:
            del(i.value)

    def __repr__(self):
        """ oooh! pretty! """

        return "-".join(map(str,self.data))
