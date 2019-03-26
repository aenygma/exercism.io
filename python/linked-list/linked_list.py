class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous

    def __repr__(self):
        return f'<{self.value}>-'

class LinkedList(object):
    def __init__(self):

        self.head = Node(None)
        self.tail = Node(None, succeeding=None, previous=self.head)
        self.head.succeeding = self.tail
        # pointer
        self.cursor = self.head
        self._length = 0

    def push(self, item):
        """ push to end of list """

        # create new node. forward to tail. previous to tail's previous
        new = Node(item, succeeding=self.tail, previous=self.tail.previous)
        self.tail.previous.succeeding = new
        self.tail.previous = new
        self._length += 1

    def pop(self):
        """ remove from end of list """

        self.cursor = self.tail.previous
        if self.cursor.value != None:
            # get value
            val = self.cursor.value
            self.cursor.succeeding.previous = self.cursor.previous
            self.cursor.previous.succeeding = self.tail
            self._length -= 1
            return val
        raise Exception("Nothing to pop")

    def shift(self):
        """ remove to start of list"""

        self.cursor = self.head.succeeding
        if self.cursor.value != None:
            val = self.cursor.value
            self.cursor.succeeding.previous = self.head
            self.cursor.previous.succeeding = self.cursor.succeeding
            self._length -= 1
            return val
        raise Exception("Nothing to shift")

    def unshift(self, item):
        """ add to start of list """

        # create new node. forward to head's next. back to head
        new = Node(item, succeeding=self.head.succeeding, previous=self.head)
        self.cursor = self.head.succeeding
        self.head.succeeding.previous = new
        self.head.succeeding = new
        self._length += 1

    def __len__(self):
        """ length of list"""

        return self._length

    def __iter__(self):
        """ iterate list """

        cur = self.head.succeeding
        while cur.succeeding != None:
            yield cur.value
            cur = cur.succeeding

    def __repr__(self):
        """ oooh. pretty! """

        cur = self.head
        ret = ""
        while cur.succeeding != None:
            ret += str(cur)
            cur = cur.succeeding
        ret += str(cur)
        return ret
