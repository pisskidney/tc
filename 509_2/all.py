#!/usr/bin/python


class PalindromizationDiv2(object):
    def pal(self, x):
        x = str(x)
        for i in range(0, len(x) / 2):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True

    def getMinimumCost(self, x):
        for i in range(0, 10**5 + 1):
            n1 = x + i
            n2 = x - i
            if self.pal(n1) or self.pal(n2):
                return i
        return -1
