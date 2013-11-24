from __future__ import division

import time

class Brain():
    # Time that events will stay in short-term memory
    time_threshold = 4

    def __init__(self):
        self.signals = []

        self.short_term_memory = []
        self.long_term_memory = [] # List of list of old signals

    def clean_short_term_memory(self):
        """ Removes short term memories that are older than time_threshold """
        now = time.time()
        self.short_term_memory = filter(lambda memory: now - memory.time_created < time_threshold, self.short_term_memory)

    def read_signals(self):
        """ Read and process new signals being received """
        # Forget old memories
        clean_short_term_memory()

        # Process all new signals into memories
        while self.signals:
            sig = self.signals.pop()
            print sig

class Short_Term_Memory():
    time_created = time.time()

    def __init__(self, signal):
        self.signal = signal

class Long_Term_Memory():
    """ A memory of signals occuring at times near each other """
    time_created = time.time()

    def __init__(self, signals):
        signals = []


class Signal():
    incentive = 0

    def difference(self):
        """ Returns the difference between this and another signal's values in a range from 0.0-1.0 """
        return 0

class Color(Signal):
    """ An RGB color with values from (0,0,0) - (255,255,255) """
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def difference(self, sig):
        #TODO: Three calls to "abs" is bad. Can we remove them in place of a single call?
        return (abs(self.r - sig.r) + abs(self.g - sig.g) + abs(self.b - sig.b)) / 3 / 255


class Incentive(Signal):
    """ An incentive with values from 0.0 - 1.0 """
    def __init__(self, intensity):
        self.intensity = intensity
        self.incentive += intensity

class Pain(Signal):
    """ A physical pain with values from 0.0 - 1.0 """
    def __init__(self, intensity):
        self.intensity = intensity
        self.incentive -= intensity

white = Color(255,255,255)
black = Color(0,0,0)
incentive = Incentive(1.0)
pain = Pain(1.0)

brain = Brain()

# Testing map
input_map = {
    "w": white,
    "b": black,
    "i": incentive,
    "p": pain,
}
while True:
    # Input Loop
    i = raw_input(" > ")
    if i in input_map:
        brain.signals.append(input_map[i])

    brain.read_signals()