#!/usr/bin/python


class CubeAnts(object):
    def getMinimumSteps(self, p):
        if 6 in p:
            return 3
        elif 2 in p or 5 in p or 7 in p:
            return 2
        elif 1 in p or 3 in p or 4 in p:
            return 1
        else:
            return 0


class CubeStickers(object):
    def isPossible(self, s):
        d = dict()
        for x in s:
            if x not in d:
                d[x] = 1
            elif d[x] < 2:
                d[x] += 1
        return 'YES' if sum(d.values()) >= 6 else 'NO'
