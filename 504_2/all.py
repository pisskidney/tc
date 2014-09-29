#!/usr/bin/python


class ComparerInator(object):
    def makeProgram(self, a, b, wanted):
        a = list(a)
        b = list(b)
        wanted = list(wanted)
        if a == wanted or b == wanted:
            return 1
        else:
            ok1 = True
            ok2 = True
            for i in xrange(len(wanted)):
                if wanted[i] != min(a[i], b[i]):
                    ok1 = False
                if w != max(a[i], b[i]):
                    ok2 = False
            if ok1 or ok2:
                return 7
        return -1


class MathContest(object):
    def countBlack(self, seq, rep):
        seq = seq * rep
        i = 0
        ans = 0
        n = len(seq)
        while i < len(seq):
            if seq[i] == 'W':
                seq = seq[:i+1] + seq[i+1:][::-1]
            else:
                ans += 1
                seq = seq[:i+1] + ''.join(['W' if x == 'B' else 'B' for x in seq[i+1:]])
            i += 1
        return ans
