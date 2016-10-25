#!/usr/bin/python


class OddDivisors():
    def f(self, x):
        if x == 1:
            return 1
        elif x == 2:
            return 2
        elif x % 2 == 0:
            return self.f(x/2)
        else:
            return x

    def findSum(self, n):
        oddsum = 0
        if n % 2 == 0:
            oddsum = (n / 2) ** 2
        else:
            oddsum = ((n + 1) / 2) ** 2
        evensum = 0
        for i in xrange(2, n + 1, 2):
            print i
            evensum += self.f(i)

        return oddsum + evensum




class MountainRoad():
    def findDistance(self, start, finish):
        l = max(finish) - min(start)
        return l*2/2**0.5


print MountainRoad().findDistance((1,), (7,))


