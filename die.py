# -*- coding: utf-8 -*-

from random import uniform
import notification

# Constants
errorAllowance = 0.000001 # how much allowance for error in dice probability

# errors
def errorCheck(faces):
    total = 0
    for face in faces:
        total += face.p
    if total < 1+errorAllowance and total > 1-errorAllowance:
        return
    else:
        notification.close("the sum of face probabilities for this die, " + str(total) +
                           ", is outside the allowed margin for error: " + str(errorAllowance))

def ChangeErrorAllowance(value):
    global errorAllowance
    errorAllowance = value
    
def SetErrorAllownanceToDefault():
    global errorAllowance
    errorAllowance = 0.000001

# Class Die is a single instance of a die, which is composed of faces. It
# takes a list of Faces as an argument
class Die:
    def __init__(self, faces):
        errorCheck(faces)
        self.faces = faces
    def roll(self):
        roll = uniform(0,1)
        total = 0
        for face in self.faces:
            total += face.p
            if roll < total:
                return face