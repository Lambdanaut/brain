import time

from signals import Short_Term_Memory, Long_Term_Memory

from collections import deque

class Brain():
    def __init__(self):
        # Number of seconds that events will stay in short-term memory
        self.time_threshold = 4.0

        # How different (from 0.0-1.0) a signal can be from another to trigger each other
        self.diff_threshold = 0.1

        # Maximum number of long term memories that will be held at a time
        # When this number is reached, the oldest long term memories are discarded
        self.long_term_memories_size = 1000

        self.short_term_memories = []
        self.long_term_memories = deque(maxlen=self.long_term_memories_size)

    def cycle(self, signal=None):
        """ Runs through a single frame of thought with a new signal """

        # Forget old short term memories
        self.clean_short_term_memory()

        # Process new signal into short term memory
        if signal != None:
            new_short_term_memory = Short_Term_Memory(signal)
            self.short_term_memories.append(new_short_term_memory)


        # Process short term memories into long term memories

        # Check for long term memory match
        short_term_memory_signals = map(lambda memory: memory.signal, self.short_term_memories)
        new_long_term_memory = Long_Term_Memory(short_term_memory_signals)

        for long_term_memory_index in range(0,len(self.long_term_memories)):
            long_term_memory = self.long_term_memories[long_term_memory_index]
            if self.match_signals(new_long_term_memory.difference(long_term_memory)):
                # If we have a match, then bring the match to the front of our long term memory
                # TODO: This remove & append is very innefficient. Try to re-write it somehow. 
                # TODO: Combine the new_long_term_memory with the matched long_term_memory
                self.long_term_memories.remove(long_term_memory)
                self.long_term_memories.append(long_term_memory)
                break
        else:
            # If no long term memory match exists, then remember a new long term memory
            self.long_term_memories.append(new_long_term_memory)

        print self.long_term_memories



    def clean_short_term_memory(self):
        """ Removes short term memories that are older than time_threshold """
        now = time.time()
        self.short_term_memories = filter(lambda memory: now - memory.time_created < self.time_threshold, self.short_term_memories)

    def match_signals(self, signal_difference):
        """ Returns true if the signals are more similar than the diff_threshold """
        return signal_difference < self.diff_threshold