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


class YetAnotherIncredibleMachine():
    def isok(self, left, right, ball):
        if left <= ball and right >= ball:
            return False
        return True

    def countWays(self, mounts, lens, balls):
        res = 1
        for i in xrange(len(mounts)):
            subres = 0
            pmin = mounts[i] - lens[i]
            pmax = mounts[i] + lens[i]
            for j in balls:
                if j <= mounts[i] and j >= pmin:
                    pmin = j + 1
                if j >= mounts[i] and j <= pmax:
                    pmax = j - 1
            if pmin >= pmax or pmax - pmin + 1 < lens[i]:
                subres = 0
            else:
                subres = pmax - pmin - lens[i] + 1

            res *= subres
            res %= 1000000009
        return res


print YetAnotherIncredibleMachine().countWays((7,), (10,), (3, 4,))
