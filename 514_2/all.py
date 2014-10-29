#!/usr/bin/python


import math


class MagicalGirlLevelOneDivTwo():
    def theMinDistance(self, d, x, y):
        mvx = x >= -d and x <= d
        mvy = y >= -d and y <= d

        if mvx and mvy:
            return 0
        if mvx:
            return abs(y) - d
        if mvy:
            return abs(x) - d
        return math.sqrt((abs(y) - d) ** 2 + (abs(x) - d) ** 2)
