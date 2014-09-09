#!/usr/bin/python

class DifferentStrings(object):
    def minimize(self, A, B):
        min_dif = 99999
        while len(B) >= len(A):
            d = self.dif(A, B)
            if d < min_dif:
                min_dif = d
            A = ' ' + A
        return min_dif

    def dif(self, A, B):
        c = 0
        for i in range(len(A)):
            if A[i] != B[i] and A[i] != ' ':
                c += 1
        return c

ds = DifferentStrings()
print 2, ds.minimize('adaabc', 'aababbc')
print 0, ds.minimize('abc', 'topabcoder')
