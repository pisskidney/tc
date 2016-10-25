#!/usr/bin/python


class MonochromaticBoard(object):
    def theMin(self, b):
        c, r = 1, 1
        for i in xrange(len(b)):
            if 'B' in b[i]:
                r += 1
        for i in xrange(len(b[0])):
            added = False
            for j in xrange(len(b)):
                if not added and b[j][i] == 'B':
                    c += 1
        return min(c, r)


print MonochromaticBoard().theMin(            (
        "WBWBW",
        "BBBBB",
        "WBWBW",
        "WBWBW"







        ))





