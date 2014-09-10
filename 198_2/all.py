#!/usr/bin/python


class Reppity(object):
    def longestRep(self, s):
        maxx = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    c = 1
                    for k in range(j + 1, len(s)):
                        if s[k] == s[i + c] and i + c < j:
                            c += 1
                        else:
                            break
                    if c > maxx:
                        maxx = c
        return maxx


class RedSquare(object):
    def countTheEmptyReds(self, maxRank, maxFile, ranks, files):
        black = (1 + maxFile) % 2
        c = 0
        pieces = zip(ranks, files)
        for i in range(1, maxRank + 1):
            for j in range(1, maxFile + 1):
                if (i + j) % 2 != black and (i, j) not in pieces:
                    c += 1
        return c


class ComplexIntegers(object):
    def prime(self, x):
        if x in [2, 3]:
            return True
        for i in range(2, int(x**(1/2.0)) + 1):
            if x % i == 0:
                return False
        return True

    def classify(self, reals, ims):
        res = []
        for r, i in zip(reals, ims):
            z = r**2 + i**2
            if z == 0:
                res.append('zero')
            elif z == 1:
                res.append('unit')
            else:
                r = abs(r)
                i = abs(i)
                if r == 0 or i == 0:
                    if (self.prime(r) and r % 4 == 3) or (self.prime(i) and i % 4 == 3):
                        res.append('prime')
                    else:
                        res.append('composite')
                else:
                    if self.prime(z):
                        res.append('prime')
                    else:
                        res.append('composite')
        return res
