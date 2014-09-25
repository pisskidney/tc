#!/usr/bin/python


class TheProgrammingContestDivTwo(object):
    def find(self, t, reqs):
        reqs = sorted(reqs)
        pen = []
        ttime = 0
        s = 0
        for x in reqs:
            pen.append(ttime + x)
            s += 1
            ttime += x
            if ttime > t:
                s -= 1
                return s, sum(pen[:-1])

        return s, sum(pen)
