#!/usr/bin/python


class TrainingCamp():
    def determineSolvers(self, a, p):
        n = len(a)
        m = len(a[0])
        k = len(p)

        res = []
        for i in xrange(n):
            comp = ''
            for j in xrange(k):
                good = True
                for kk in xrange(m):
                    if p[j][kk] == 'X' and a[i][kk] == '-':
                        good = False
                comp += 'X' if good else '-'
            
            res.append(comp)
        return res

