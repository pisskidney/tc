#!/usr/bin/python

from collections import deque

class Target(object):
    def draw(self, n):
        s = deque(["#####", "#   #", "# # #", "#   #", "#####"])
        if n == 5:
            return s
        for i in range(1, (n / 4)):
            for x in range(len(s)):
                s[x] = '# ' + s[x] + ' #'
            s.appendleft('#' + ' ' * (5 + i * 4 - 2) + '#')
            s.appendleft('#' * (5 + i * 4))
            s.append('#' + ' ' * (5 + i * 4 - 2) + '#')
            s.append('#' * (5 + i * 4))
        
        return s


from math import sqrt


class Jumping(object):
    def ableToGet(self, x, y, jumps):
        dist = sqrt(x*x + y*y)
        if sum(jumps) < dist:
            return 'Not able'
        elif len(jumps) == 1 and sum(jumps) > dist:
            return 'Not able'
        r = [jumps[0], jumps[0]]
        for x in jumps[1:]:
            r[0] = abs(abs(r[0]) - x)
            r[1] = abs(abs(r[1] + x))

        if dist >= r[0] and dist <= r[1]:
            return 'Able'
        return 'Not Able'
