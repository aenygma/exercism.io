class ObserverObject(object):
    """ An observer class
    """

    def __init__(self):
        self.observers = []

    def register_observer(self, ob):
        self.observers.append(ob)

    def unregister_observer(self, ob):
        self.observers.remove(ob)

    def notify_observers(self):
        for observer in self.observers:
            if DEBUG:
                print(self, "notifying", observer)
            observer.update()

    def update(self):
        raise NotImplementedError

class InputCell(ObserverObject):
    def __init__(self, initial_value, name=None):
        ObserverObject.__init__(self)
        self._value = initial_value
        self._name = ic_val() if name==None else name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        if self._value == newvalue:
            return
        self._value = newvalue
        self.notify_observers()

    def update(self):
        pass

    def __repr__(self):
        return f'<{self._name}: Value = {self._value}>'

class ComputeCell(ObserverObject):
    def __init__(self, inputs, compute_function, name=None):
        # init the observer inheritance
        ObserverObject.__init__(self)

        # stash away
        self.inputs = inputs
        self.cf = compute_function
        self.cbs = []
        self._value = None
        self._name = cc_val() if name==None else name

        # register our depenendants
        for i in inputs:
            i.register_observer(self)

        # calculate value
        self.value

    @property
    def value(self):
        # compute
        ret = self.cf([x.value for x in self.inputs])

        # don't percolate changes if value didn't change
        if ret == self._value:
            return self._value
        self._value = ret

        # do callbacks
        for cb in self.cbs:
            if DEBUG:
                print(self, "firing cb")
            cb(self._value)

        # notify
        self.notify_observers()
        return self._value

    def update(self):
        return self.value

    def __repr__(self):
        return f'<{self._name}>'

    def add_callback(self, callback):
        self.cbs.append(callback)

    def remove_callback(self, callback):
        if callback in self.cbs:
            self.cbs.remove(callback)

#
# Helpers for debugging
#
def mk_name(t):
    val = 0
    def ic():
        nonlocal val
        val += 1
        return f'{t}: {val}'
    return ic
ic_val = mk_name("Input Cell")
cc_val = mk_name("Compute Cell")
DEBUG = False
# /Helpers for debugging


