# -*- coding: utf-8 -*-

# class Face is a container for the probability (p) and values of a particular 
# face of a die.
# It contains a container (.values) for the myriad values that could be encoded
# on the side of the die. E.g. colors, symbols, number pips etc.
# "number" is the default keyword for a numeric face value
# "color" is the default keyword for a face's color value
# All keywords must be strings and their respective values should be integers. 
class Face:
    def __init__(self, p, **kwargs):
        self.p = p # the probability of the face being hit
        self.values = {} # contains attributes of the face and their values
        for key in kwargs.keys():
            self.values[key] = kwargs[key]
    def getValue(self, attribute):
        if attribute in self.values.keys():
            return self.values[attribute]
        else:
            return 0
        
"""
f = Face(0.5, number=1) # coin
f = Face(0.25, number=3) # 1-face of a 4 sided die

# Example of complicated dice (challenge dice from Warhammer Fantasy RPG 5e)
f = Face(1/8, skull=1)
f = Face(1/8, chaos=1)
f = Face(1/8, sword=1)
f = Face(1/8, sword=2)
"""