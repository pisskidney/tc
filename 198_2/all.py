#!/usr/bin/python


import math


class ComputationalComplexity(object):
    def fastestAlgo(self, c, p, l, n):
        minind = 0
        minv = 9999999999999999999
        for i in range(len(c)):
            x = c[i] * n**p[i] * math.log(n)**l[i]
            if x < minv:
                minv = x
                minind = i
        return minind


class Generators(object):
    def find(self, p):
        z = set([i for i in range(1, p)])
        res = []
        for i in range(2, p):
            g = [1]
            f = i
            for j in range(1, p - 1):
                g.append(f)
                f *= i
                f %= p
            if set(g) == z:
                res.append(i)
        return res


print Generators().find(937)


