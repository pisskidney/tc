#!/usr/bin/python


import math

class ClapLight(object):
    def light(self, d, t):
        for i in range(3, len(d)):
            if d[i] < t and d[i - 1] >= t and d[i - 2] >= t and d[i - 3] < t:
                return True
        return False

    def threshold(self, d):
        d_ = sorted(d)

        t = d_[int(math.ceil(len(d_)/2))] + 1

        x = sorted(list(set(d)))

        while self.light(d, t) and t <= max(d):
            t = x[x.index(t - 1) + 1] + 1

        if self.light(d, t):
            return None

        return t


cl = ClapLight()
print cl.threshold([5,8,7,6,12,8,4,3,2,6])
print cl.threshold([6, 6, 6, 6, 6])


