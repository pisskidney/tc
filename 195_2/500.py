#!/usr/bin/python


class FanFailure(object):
    def getRange(self, d, t):
        d = sorted(d, reverse=True)
        s = 0
        mfs = 0
        mfc = 0
        for i in range(len(d)):
            s += d[i] 
            if s >= t:
                mfs = len(d) - 1 - i
                break
        total = sum(d)
        for i in range(len(d)):
            if total - d[i] >= t:
                mfc += 1
                total -= d[i]
            else:
                break
        return mfs, mfc


ff = FanFailure()
print ff.getRange((1, 2, 3), 2)
