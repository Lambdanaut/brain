from __future__ import division

import time


class Signal(object):
    def difference(self, sig):
        """ Returns the difference between this and another signal's values in a range from 0.0 - 1.0 """
        raise NotImplementedError

    def combine(self, sig):
        """ Returns a signal to represent a "combined" form of this signal and another signal's values. """
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.__repr__()


class Color(Signal):
    """ An RGB color with values from (0,0,0) - (255,255,255) """
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def difference(self, sig):
        #TODO: Three calls to "abs" is bad. Can we remove them in place of a single call?
        return (abs(self.r - sig.r) + abs(self.g - sig.g) + abs(self.b - sig.b)) / 3 / 255

    def combine(self, sig):
        r = (self.r + sig.r) / 2
        g = (self.g + sig.g) / 2
        b = (self.b + sig.b) / 2
        new_color = Color(r, g, b)
        return new_color

    def __repr__(self):
        return "{} ({}, {}, {})".format(self.__class__.__name__, str(self.r), str(self.g), str(self.b))


class Feeling(Signal):
    """ A positive or negative feeling with values from -1.0 - 1.0 """
    def __init__(self, intensity):
        self.intensity = intensity

    def difference(self, sig):
        """
        Returns 1.0 if the signals are not of the same type (incentive/pain).
        Returns the numerical difference otherwise.
        """
        return min(abs(self.intensity - sig.intensity), 1.0)

    def combine(self, sig):
        new_feeling = Feeling((self.intensity + sig.intensity) / 2)

        return new_feeling

    def __repr__(self):
        return "{} ({})".format(self.__class__.__name__, self.intensity)


class Short_Term_Memory():

    def __init__(self, signal):
        self.signal = signal

        self.time_created = time.time()


class Long_Term_Memory(Signal):
    """ A memory of signals occuring at times near each other """
    def __init__(self, signals):
        self.signals = signals

        now = time.time()
        self.time_created = now
        # self.last_recalled = now

    def difference(self, comparing_sig):
        """ Returns an average difference of all signals of the same types of both lists """

        len_self_signals = len(self.signals)
        len_comparing_signals = len(comparing_sig.signals)

        # Gets the difference in length between the two signal lists from 0.0 - 1.0. 
        # If the len_diff is greater than 10, set the difference to 1.0
        len_diff = min(abs(len_self_signals - len_comparing_signals) / 10, 1.0)

        # Ensure that we always loop through the smaller list first
        outer_loop = self.signals
        inner_loop = comparing_sig.signals

        if len_self_signals > len_comparing_signals:
            outer_loop, inner_loop = inner_loop, outer_loop

        dif = 0.0 + len_diff

        for sig1 in outer_loop:
            closest_match = 1.0
            for sig2 in inner_loop:
                if sig1.__class__.__name__ == sig2.__class__.__name__:
                    sigdif = sig1.difference(sig2)
                    if sigdif < closest_match:
                        closest_match = sigdif
            dif += closest_match

        return dif / (len(outer_loop) + 1) # The +1 is for len_diff

    def combine(self, combining_sig):
        """ Combines every signal's closest match to create a new ltm """

        # Return an empty ltm if either of the input ltm is empty
        if not combining_sig.signals or not self.signals:
            return Long_Term_Memory([])

        # Ensure that we always loop through the smaller list first
        outer_loop = self.signals
        inner_loop = combining_sig.signals

        if len(self.signals) > len(combining_sig.signals):
            outer_loop, inner_loop = inner_loop, outer_loop

        new_ltm_signals = []
        for sig1 in outer_loop:
            closest_match_diff = 1.0
            closest_match_signal = None
            for sig2 in inner_loop:
                if sig1.__class__.__name__ == sig2.__class__.__name__:
                    sigdif = sig1.difference(sig2) 
                    if sigdif < closest_match_diff:
                        closest_match_diff = sigdif
                        closest_match_signal = sig2
            if closest_match_signal:
                new_combined_signal = closest_match_signal.combine(sig1)
                new_ltm_signals.append(new_combined_signal)

        new_ltm = Long_Term_Memory(new_ltm_signals)
        return new_ltm

    def __str__(self):
        return str(self.signals)

    def __repr__(self):
        return self.__str__()
