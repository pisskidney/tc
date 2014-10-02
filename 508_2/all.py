#!/usr/bin/python


class CandyShop(object):
    def countProbablePlaces(self, x, y, r):
        ans = 0
        for i in xrange(-200, 201):
            for j in xrange(-200, 201):
                good = True
                for k in xrange(len(x)):
                    if good and (abs(x[k] - i) + abs(y[k] - j) > r[k]):
                        good = False
                ans += good
        return ans
