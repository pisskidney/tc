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
            for j in xrange(mounts[i] - lens[i], mounts[i] + 1):
                ok = True
                for k in balls:
                    if not self.isok(j, j + lens[i], k):
                        ok = False
                        break
                if ok:
                    subres += 1
            res *= subres
            res %= 1000000009
        return res


print YetAnotherIncredibleMachine().countWays([0]*50, [10000]*50, range(1, 51))
print YetAnotherIncredibleMachine().countWays((0,), (1,), (0,))




