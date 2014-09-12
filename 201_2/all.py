#!/usr/bin/python


class Multiples(object):
    def number(self, minn, maxx, fac):
        res = 0
        for x in xrange(minn, maxx + 1):
            if not x % fac:
                res += 1
        return res


class ElevatorLimit(object):
    def getRange(self, on, off, l):
        minn = -1
        maxx = -1
        for i in range(l + 1):
            c = i
            ok = True
            for j in range(len(on)):
                c -= off[j]
                if c < 0:
                    ok = False
                    break
                c += on[j]
                if c > l:
                    ok = False
                    return [minn, maxx] if minn != -1 else []
            if ok:
                if minn == -1:
                    minn = i
                maxx = i
        return [minn, maxx] if minn != -1 else []
