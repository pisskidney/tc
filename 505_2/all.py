#!/usr/bin/python


class SentenceCapitalizerInator(object):
    def fixCaps(self, p):
        p = p[0].upper() + p[1:]
        for i in range(1, len(p)):
            if p[i] == '.' and i != len(p) - 1:
                p = p[:i+2] + p[i+2].upper() + p[i + 3:]
        return p


class PerfectSequences(object):
    def fixIt(self, s):
        if len(s) == 1:
            return 'Yes'
        for i in xrange(len(s)):
            p = 1
            for j in xrange(len(s)):
                if i != j and p < 10**12:
                    p *= s[j]
            q = 0
            for j in xrange(len(s)):
                if i != j:
                    q += s[j]

            ans = -1
            if p == 0 and q == 0:
                ans = 0
            elif (p - 1) != 0:
                ans = float(q)/(p - 1)
            if ans >= 0 and int(ans) == ans and ans != s[i]:
                return 'Yes'
        return 'No'
