import time

from signals import Short_Term_Memory, Long_Term_Memory

class Brain():
    # Number of seconds that events will stay in short-term memory
    time_threshold = 4

    # How different (from 0.0-1.0) a signal can be from another to trigger each other
    diff_threshold = 0.5

    long_term_memory_size = 1000

    def __init__(self):
        self.signals = []

        self.short_term_memory = []
        self.long_term_memory = [] # List of lists of old signals

    def clean_short_term_memory(self):
        """ Removes short term memories that are older than time_threshold """
        now = time.time()
        self.short_term_memory = filter(lambda memory: now - memory.time_created < time_threshold, self.short_term_memory)

    def read_signals(self):
        """ Read and process new signals being received """
        # Forget old memories
        self.clean_short_term_memory()

        # Process all new signals into short term memories
        while self.signals:
            new_memory = Short_Term_Memory(self.signals.pop())
            self.short_term_memory.append(new_memory)

        # Process short term memories into long term memories
        for memoryX in self.short_term_memory:
            new_longterm_memory = []
            for memoryY in self.short_term_memory:
                if id(memoryX) != id(memoryY):

    def match_signals(self, signal_difference):
        """ Returns true if the signals are more similar than the diff_threshold """
        return signal_difference < self.diff_threshold