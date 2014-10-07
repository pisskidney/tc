#!/usr/bin/python

import math


class SimpleWordGame():
    def points(self, p, d):
        counted = {}
        ans = 0
        for x in p:
            if x not in counted and x in d:
                counted[x] = True
                ans += len(x)*len(x)
        return ans


class Underprimes():
    def howMany(self, A, B):
        ans = 0

        for i in xrange(A, B+1):
            c = 0
            d = 2
            x = i
            while x > 1:
                if d * d > x:
                    c += 1
                    break
                if x % d == 0:
                    x /= d
                    c += 1
                else:
                    if d > 2:
                        d += 1
                    d += 1
            if c in (2, 3, 5, 7, 11, 13):
                ans += 1
        return ans


print Underprimes().howMany(2, 100000)
