#!/usr/bin/python


class LastDigit:
    def findX(self, S):
        def calc(x):
            if x/10:
                return x + calc(x/10)
            return x
        lo, hi = 0, S
        while lo <= hi:
            mid = (lo+hi)/2
            x = calc(mid)
            if x == S:
                return mid
            elif calc(mid) < S:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


ld = LastDigit()
print ld.findX(999999999999999999)


