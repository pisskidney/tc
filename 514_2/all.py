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


class MagicalGirlLevelTwoDivTwo():
    def isReachable(self, jumps, x, y):
        q = [(0, 0)]
        visited = set([(0, 0)])
        c = 0
        while q:
            current = q.pop()
            for j in jumps:
                dx = (1, -1, 1, -1, j, j, -j, -j)
                dy = (j, j, -j, -j, 1, -1, 1, -1)
                for i in xrange(len(dx)):
                    newx = current[0] + dx[i]
                    newy = current[1] + dy[i]
                    new = (newx, newy)
                    if new not in visited and abs(newx) <= 60 and abs(newy) <= 60:
                        visited.add(new)
                        q.append(new)
                        c += 1
        return 'YES' if (x, y) in visited else 'NO'

print MagicalGirlLevelTwoDivTwo().isReachable((2,), 5, 4)

