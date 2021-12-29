# -*- coding: utf-8 -*-

class Pool:
    def __init__(self, dice):
        self.dice = dice
    def roll(self):
        results = {}
        for die in self.dice:
            result = die.roll()
            for key in result.values:
                if key in results.keys():
                    results[key] += result.values[key]
                else:
                    results[key] = result.values[key]
        return results

"""
Example:
    
from Face import Face
from Die import Die

faces = []
faces.append(Face(0.25, number = 1, green = 1))
faces.append(Face(0.25, number = 2, blue = 1))
faces.append(Face(0.25, number = 3))
faces.append(Face(0.25, number = 4))
die = Die(faces)
pool = Pool([die,die,die])
r = pool.roll()
"""