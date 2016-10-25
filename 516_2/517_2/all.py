#!/usr/bin/python


class MonochromaticBoard():
    def theMin(self, b):
        if 'W' not in ''.join(b):
            return min(len(b), len(b[0]))
        res = 0
        for i in xrange(len(b)):
            if 'W' not in b[i]:
                res += 1
        if res == len(b):
            return res
        for i in xrange(len(b[0])):
            if 'W' not in [b[j][i] for j in xrange(len(b))]:
                res += 1
        return res


class CompositeSmash():
    def thePossible(self, n, t):
        dp = [False for _ in xrange(len(n) + 1)]
        dp[t] = True
        for i in xrange(t + 1, n + 1):



print CompositeSmash().thePossible(16, 10)

