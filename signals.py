from __future__ import division

import time

class Signal():
    def difference(self, sig):
        """ Returns the difference between this and another signal's values in a range from 0.0 - 1.0 """
        raise NotImplementedError

    def combine(self, sig):
        """ Alters this signal to represent a "combined" form of this signal and another signal's values. """
        raise NotImplementedError

    @property
    def incentive(self):
        """ A measure of how desireable the signal is to feel or avoid from -1.0 - 1.0 """
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

    def combine(self, sig):
        self.r = (self.r + sig.r) / 2
        self.g = (self.g + sig.g) / 2
        self.b = (self.b + sig.b) / 2


class Feeling():
    def __init__(self, intensity):
        self.intensity = intensity

    def difference(self, sig):
        """
        Returns 1.0 if the signals are not of the same type (incentive/pain).
        Returns the numerical difference otherwise.
        """
        return min(abs(self.incentive - sig.incentive), 1.0)

    def combine(self, sig):
        this.intensity += sig.intensity
        this.intensity /= 2


class Incentive(Feeling, Signal):
    """ An incentive with values from 0.0 - 1.0 """
    @property
    def incentive(self):
        return 0 + self.intensity


class Pain(Feeling, Signal):
    """ A physical pain with values from 0.0 - 1.0 """
    @property
    def incentive(self):
        return 0 - self.intensity


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

        # TODO: Write a good description of what the fuck is going on here.

        # Gets the difference in length between the two signal lists from 0.0 - 1.0. 
        # If the len_diff is greater than 5, set the difference to 1.0
        len_diff = min(abs(len(self.signals) - len(comparing_sig.signals)) / 10, 1.0)

        dif = 0.0 + len_diff

        for sig1 in self.signals:
            closest_match = 1.0
            for sig2 in comparing_sig.signals:
                if sig1.__class__.__name__ == sig2.__class__.__name__:
                    sigdif = sig1.difference(sig2) 
                    if sigdif < closest_match:
                        print str(closest_match) + ": " + sig1.__class__.__name__ + " " + str(sigdif)
                        closest_match = sigdif
            dif += closest_match

        return dif / (len(self.signals) + 1) # The +1 is for len_diff
