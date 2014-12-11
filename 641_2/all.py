#!/usr/bin/python


class BuyingTshirts(object):
    def meet(self, t, q, p):
        qq = list()
        pp = list()
        s = 0
        for i in xrange(len(q)):
            s += q[i]
            if s >= t:
                s -= t
                qq.append(i)
        s = 0
        for i in xrange(len(p)):
            s += p[i]
            if s >= t:
                s -= t
                pp.append(i)

        print qq, pp
        res = 0
        for day in qq:
            if day in pp:
                res += 1
        return res


class TrianglesContainOriginEasy(object):
    def area(self, x1, y1, x2, y2, x3, y3):
        return abs( (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0)


    def count(self, x, y):
        res = 0
        for i in xrange(len(x)):
            for j in xrange(i + 1, len(x)):
                for k in xrange(j + 1, len(x)):
                    if self.area(x[i], y[i], x[j], y[j], x[k], y[k]) == self.area(0, 0, x[j], y[j], x[k], y[k]) + self.area(x[i], y[i], 0, 0, x[k], y[k]) + self.area(x[i], y[i], x[j], y[j], 0, 0):
                        res += 1
        return res


class ShufflingCardsDiv2(object):
    def shuffle(self, p):
        d1 = []
        d2 = []
        mid = len(p)/2 + 0.5
        for i in xrange(len(p)):
            if i < len(p)/2:
                if i % 2 == 0:
                    d1.append('s')
                else:
                    d1.append('b')
            else:
                if i % 2 == 0:
                    d2.append('s')
                else:
                    d2.append('b')
        for i in xrange(len(p)):
            try:
                if i % 2 == 0:
                    if p[i] < mid:
                        d1.remove('s')
                    else:
                        d1.remove('b')
                else:
                    if p[i] < mid:
                        d2.remove('s')
                    else:
                        d2.remove('b')
            except ValueError:
                return 'Impossible'
        return 'Possible'


print ShufflingCardsDiv2().shuffle((8,5,4,9,1,7,6,10,3,2))







