from __future__ import division

from brain import *
from signals import Color, Feeling

# Pre-defined signals to feed into the brain
white = Color(255,255,255)
black = Color(0,0,0)
grey = Color(10,10,10)
incentive = Feeling(1.0)
pain = Feeling(-1.0)

def main():
    brain = Brain()

    # Testing map
    input_map = {
        "w": white,
        "b": black,
        "g": grey,
        "i": incentive,
        "p": pain,
    }

    while True:
        # Input Loop
        i = raw_input(" > ")
        if i in input_map:
            input_signal = input_map[i]
            print ("Adding new {}".format(input_signal.__class__.__name__))
            brain.cycle(input_signal)
        else: 
            brain.cycle()


if __name__ == "__main__":
    main()