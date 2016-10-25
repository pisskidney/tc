#!/usr/bin/python


class DifferentStrings():
    def minimize(self, A, B):
        res = len(A)
        for i in xrange(len(B) - len(A) + 1):
            c = 0
            for j in xrange(len(A)):
                if A[j] != B[i+j]:
                    c += 1
            res = min(res, c)
        return res

print DifferentStrings().minimize('koder', 'topcoder')



