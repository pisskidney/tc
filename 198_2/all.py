#!/usr/bin/python


class Reppity(object):
    def longestRep(self, s):
        maxx = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    c = 1
                    for k in range(j + 1, len(s)):
                        if s[k] == s[i + c] and i + c < j:
                            c += 1
                        else:
                            break
                    if c > maxx:
                        maxx = c
        return maxx


class RedSquare(object):
    def countTheEmptyReds(self, maxRank, maxFile, ranks, files):
        black = (1 + maxFile) % 2
        c = 0
        pieces = zip(ranks, files)
        for i in range(1, maxRank + 1):
            for j in range(1, maxFile + 1):
                if (i + j) % 2 != black and (i, j) not in pieces:
                    c += 1
        return c


print RedSquare().countTheEmptyReds(50, 50, [1], [1])
