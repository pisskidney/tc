#!/usr/bin/python


class SentenceCapitalizerInator(object):
    def fixCaps(self, p):
        p = p[0].upper() + p[1:]
        for i in range(1, len(p)):
            if p[i] == '.' and i != len(p) - 1:
                p = p[:i+2] + p[i+2].upper() + p[i + 3:]
        return p
