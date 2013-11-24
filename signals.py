from __future__ import division

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