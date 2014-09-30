#!/usr/bin/python


class SlimeXSlimeRancher2(object):
    def train(self, a):
        ma = max(a)
        ans = 0
        for x in a:
            ans += (ma - x)
        return ans


class SlimeXSlimesCity(object):
    def merge(self, pop):
        pop = sorted(pop, reverse=True)
        for i in xrange(len(pop) - 1):
            if pop[i] > sum(pop[i + 1:]):
                return i + 1
        return len(pop)
