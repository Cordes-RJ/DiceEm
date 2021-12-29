# -*- coding: utf-8 -*-

from Face import Face
from Die import Die
from Pool import Pool
# errors

# MakeFairDie creates a fair die given a number of sides
def MakeFairDie(sides):
    p = 1/sides
    faces = []
    for i in range(sides):
        faces.append(Face(p,number=i+1))
    return Die(faces)

# decodeDieString creates a die pool from a text string e.g. 2d6, 3d20
def decodeDieString(dieString):
    ad = False # after delimiter
    number = ""
    sides = ""
    for i in dieString:
        if i == "d":
            ad = True
        elif ad:
            sides += i
        else:
            number += i
    number = int(number)
    sides  = int(sides)
    diePool = []
    for i in range(number):
        diePool.append(MakeFairDie(sides))
    return diePool
    
# makeFairDiePoolFromText creates a die pool from a text string e.g. 2d6, 3d20
def makeFairDiePoolFromText(*args):
    dice = []
    for dieString in args:
        d = decodeDieString(dieString)
        for i in d:
            dice.append(i)
    return Pool(dice)

# p = makeFairDiePoolFromText("4d6","1d20")