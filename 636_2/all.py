#!/usr/bin/python


class GameOfStones():
    def count(self, s):
        if len(s) == 1:
            return 0
        if max(s) == min(s):
            return 0
        if sum(s) % len(s) != 0:
            return -1

        av = sum(s) / len(s)
        for nr in s:
            if abs(av - nr) % 2 != 0:
                return -1

        s = list(s)

        c = 0

        while True:
            maxx = max(s)
            minn = min(s)
            s[s.index(maxx)] -= 2
            s[s.index(minn)] += 2

            c += 1

            if max(s) == min(s):
                return c


print ','.join([str(x) for x in [2]*50 + [98] * 50])

'''
import random
y = GameOfStones()
for _ in xrange(10000):
    lenn = random.randint(1, 100)
    ffs = []
    for _ in xrange(1, lenn+1):
        ffs.append(random.randint(1, 100))
    print 'trying: ', ffs, y.count(ffs)






import itertools
class SortishDiv2:
    def sortedness(self, seq):
        c = 0
        for i in xrange(len(seq)):
            for j in xrange(i + 1, len(seq)):
                if seq[i] < seq[j]:
                    c += 1
        return c

    def fill(self, gaps, seq):
        new = []
        for i in xrange(len(seq)):
            if seq[i] != 0:
                new.append(seq[i])
            else:
                new.append(gaps.pop())
        return new

    def ways(self, sort, seq):
        c = 0
        seq = list(seq)
        if 0 not in seq:
            if self.sortedness(seq) == sort:
                return 1
            else:
                return 0
        gaps = []
        for i in xrange(1, len(seq) + 1):
            if i not in seq:
                gaps.append(i)

        for x in itertools.permutations(gaps):
            y = list(x)
            ss = self.fill(y, seq)
            if self.sortedness(ss) == sort:
                c += 1
        return c

'''
