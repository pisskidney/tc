#!/usr/bin/python


class SRMCards(object):
    def maxTurns(self, srms):
        i = 0
        c = 0
        srms = sorted(srms)
        while i < len(srms):
            if i != len(srms) - 1 and srms[i+1] == srms[i] + 1:
                c += 1
                i += 2
            else:
                c += 1
                i += 1
        return c
