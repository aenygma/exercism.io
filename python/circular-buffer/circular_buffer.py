from collections import deque

class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass

class CircularBuffer(object):
    """ implement a circular buffer """

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def read(self):
        """ read from current location """

        if len(self.buffer) == 0:
            raise BufferEmptyException("Buffer Empty")
        return self.buffer.popleft()

    def write(self, data):
        """ write to current location """

        if len(self.buffer) == self.capacity:
            raise BufferFullException("Buffer full")
        self.buffer.append(data)

    def overwrite(self, data):
        """ sudo write to location """

        try:
            self.write(data)
        except BufferFullException as e:
            self.read()
            self.write(data)

    def clear(self):
        """ clear buffer """

        self.buffer.clear()

    def __repr__(self):
        """ oooh! pretty! """

        return "-".join(map(str, self.buffer))
