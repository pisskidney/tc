#!/usr/bin/python


class PotentialGeometricSequence(object):
    def numberOfSubsequences(self, d):
        n = len(d)
        c = 0
        for i in range(3, n + 1):
            for j in range(0, n - i + 1):
                c += self.check(d[j:j+i])
        c += n*(n+1)/2 - (n-2)*(n-1)/2
        return c

    def check(self, d):
        ffs = list()
        q = -1
        for i in range(0, len(d)):
            ffs.append(1 << d[i])
        for i in range(1, len(d)):
            x = ffs[i] / ffs[i - 1]
            if q == -1:
                q = x
            if x != q and q != -1:
                return 0
        return 1

p = PotentialGeometricSequence()
a = (1,3,5,5,5,5,64,4,23,2,3,4,5,4,3)
b = (1,2,4,8,16)
print p.numberOfSequences(b)
