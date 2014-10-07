#!/usr/bin/python

import collections


class SoccerLeagues():
    def points(self, m):
        res = [0 for _ in range(len(m))]
        for i in xrange(len(m)):
            for j in xrange(len(m)):
                if m[i][j] == 'W':
                    res[i] += 3
                elif m[i][j] == 'D':
                    res[i] += 1
                    res[j] += 1
                elif m[i][j] == 'L':
                    res[j] += 3
        return res


class CirclesCountry():
    def leastBorders(self, X, Y, R, x1, y1, x2, y2):
        c = 0
        for i in range(len(X)):
            sin = False
            din = False
            if (x1 - X[i]) ** 2 + (y1 - Y[i]) ** 2 < R[i] ** 2:
                sin = True
            if (x2 - X[i]) ** 2 + (y2 - Y[i]) ** 2 < R[i] ** 2:
                din = True
            if (sin and not din) or (not sin and din):
                c += 1
        return c


print CirclesCountry().leastBorders((0,-6,6), (0,1,2), (2,2,2), -5, 1, 5, 1)


