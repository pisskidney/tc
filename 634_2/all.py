#!/usr/bin/python


class MountainRanges(object):
    def countPeaks(self, h):
        c = 0
        if len(h) == 1:
            return 1
        for i in range(len(h)):
            if i == 0:
                if h[i + 1] < h[i]:
                    c += 1
            elif i == len(h) - 1:
                if h[i - 1] < h[i]:
                    c += 1
            else:
                if h[i - 1] < h[i] and h[i + 1] < h[i]:
                    c += 1
        return c


class SpecialStrings(object):
    def ok(self, s):
        for i in range(1, len(s)):
            if s[:i] >= s[i:]:
                return False
        return True

    def findNext(self, s):
        n = len(s)
        ss = int(s, 2)
        while ss < 2**n - 1:
            ss += 1
            s = str(bin(ss))[2:]
            if len(s) < n:
                s = '0' * (n - len(s)) + s
            if self.ok(s):
                return s
        return ''

#print SpecialStrings().findNext('1011' * 8)
print '0010' * 12
            

        




