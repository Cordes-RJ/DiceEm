# -*- coding: utf-8 -*-

import notification
 
# errors
def errorCheckP(p):
    if type(p) != float:
        notification.close("Error: "+ str(p) + ", is not a float. All probabilities must be floats")

def errorCheckKWs(keyword, value):
    if type(keyword) != str:
        notification.close("Error: "+ str(keyword) + " used as a keyword in a Face's Value Container. Keyword must be a string.")
    if type(value) != int:
        notification.close("Error: "+ str(keyword) +"'s value, " + str(value) + ", is not an integer. All values must be integers.")


# class Face is a container for the probability (p) and values of a particular 
# face of a die.
# It contains a container (.values) for the myriad values that could be encoded
# on the side of the die. E.g. colors, symbols, number pips etc.
# "number" is the default keyword for a numeric face value
# "color" is the default keyword for a face's color value
# All keywords must be strings and their respective values should be integers.
# Error handling will inform where incorrect value types are used. 
class Face:
    def __init__(self, p, **kwargs):
        errorCheckP(p)
        self.p = p # the probability of the face being hit
        self.values = {} # contains attributes of the face and their values
        for key in kwargs.keys():
            errorCheckKWs(key, kwargs[key])
            self.values[key] = kwargs[key]
    # returns the value of a particular attribute, returns 0 if attribute not present
    def getValue(self, attribute):
        if attribute in self.values.keys():
            return self.values[attribute]
        else:
            return 0
    # returns all attribute values in an array
    def getValues(self):
        values = []
        for key in self.values.keys():
            values.append([key, self.values[key]])
        return values
        
        
        
"""
f = Face(0.5, number=1) # coin
f = Face(0.25, number=3) # 1-face of a 4 sided die

# Example of complicated dice (challenge dice from Warhammer Fantasy RPG 5e)
f = Face(1/8, skull=1)
f = Face(1/8, chaos=1)
f = Face(1/8, sword=1)
f = Face(1/8, sword=2)
"""
