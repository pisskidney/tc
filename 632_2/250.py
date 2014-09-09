#!/usr/bin/python


class RunningAroundPark(object):
    def numberOfLap(self, N, d):
        c = 1
        for i in range(1, len(d)):
            if d[i] <= d[i - 1]:
                c += 1
        return c


rap = RunningAroundPark()
print rap.numberOfLap(2, (1, 3, 5, 7, 9, 2, 4, 6, 8, 10))
