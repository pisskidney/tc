#!/usr/bin/python


class FourBlocksEasy():
    def maxScore(self, g):
        ans = 0
        ids = [0 for i in xrange(len(g[0]))]

        for i in xrange(0, len(g[0])):
            if g[0][i] == '1' or g[1][i] == '1':
                ids[i] = 1
        k = 0
        while k < len(ids):
            if ids[k] == 1:
                ids[k] = 1
                ans += 2
                k += 1
            else:
                if k + 1 < len(ids) and ids[k + 1] != 1:
                    ids[k] = 4
                    ids[k+1] = 4
                    ans += 16
                    k += 2
                else:
                    ids[k] = 1
                    ans += 2
                    k += 1
        return ans


print FourBlocksEasy().maxScore(("..1.....1.....1.....1........1...1.1....1...", "1........1....1..1.....1......1..11..11....."))
