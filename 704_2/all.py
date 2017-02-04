#!/usr/bin/python


class SwapAndArithmetic(object):
    def able(self, x): 
        x = sorted(x)
        diff = None
        for i in xrange(1, len(x)):
            if diff is None:
                diff  = x[i] - x[i-1]
            elif diff != x[i] - x[i-1]:
                return 'Impossible'
        return 'Possible'


class ConnectedComponentConstruction:
    def construct(self, s):
        ind = sorted(range(len(s)), key=lambda x: s[x], reverse=True)
        s = sorted(s, reverse=True)
        i = 0
        res = [['N' for _ in xrange(len(s))] for _ in xrange(len(s))]
        while i < len(s):
            for j in xrange(1, s[i]):
                if i + j >= len(s) or s[i+j] != s[i]:
                    return []
            i += s[i]

        i = 0
        while i < len(s) and s[i] > 1:
            j = i + s[i] - 1
            for k in xrange(i, j):
                for p in xrange(k + 1, j + 1):
                    res[ind[k]][ind[p]] = 'Y'
                    res[ind[p]][ind[k]] = 'Y'
            i += s[i]

        return [''.join(res[i]) for i in xrange(len(res))]


s = ConnectedComponentConstruction()
print s.construct([2,1,1,2,1])

