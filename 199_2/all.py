#!/usr/bin/python


class StringMult(object):
    def times(self, s, k):
        res = ""
        if not s or not k:
            return ""
        if k > 0:
            for i in range(k):
                res += s
        else:
            for i in range(abs(k)):
                res += s[::-1]

        return res


class TriangleCount(object):
    def g(self, i, j):
        return j - i + 1

    def count(self, n):
        c = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                g1 = self.g(i, j)
                g2 = self.g(i, j - i)
                g1 = g1 if g1 >= 0 else 0
                g2 = g2 if g2 >= 0 else 0
                c += g1 + g2
        return c


print TriangleCount().count(4)
