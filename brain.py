import time

from signals import *

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
        self.clean_short_term_memory()

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