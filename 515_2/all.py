#!/usr/bin/python


class FortunateNumbers():
    def getFortunate(self, a, b, c):
        res = set([])
        for i in xrange(len(a)):
            for j in xrange(len(b)):
                for k in xrange(len(c)):
                    x = str(a[i]+b[j]+c[k])
                    if x.count('8') + x.count('5') == len(x) and x not in res:
                        res.add(x)
        return len(res)
