#!/usr/bin/python


class LetterStrings(object):
    def sum(self, strings):
        c = 0
        for s in strings:
            s = s.replace('-', '')
            c += len(s)
        return c


class Hyphenated(object):
    def avgLength(self, strings):
        s = ''
        c = 0
        l = 0
        for x in strings:
            if x[-1] != '-' or len(x) < 2:
                s += x
                s += ' '
            else:
                s += x[:-1]
        s = s.replace('-', ' ')
        s = s.replace('.', ' ')
        for x in s.split(' '):
            if x:
                c += 1
                l += len(x)
        return l / float(c)
