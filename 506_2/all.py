#!/usr/bin/python


class SlimeXSlimeRancher2(object):
    def train(self, a):
        ma = max(a)
        ans = 0
        for x in a:
            ans += (ma - x)
        return ans
