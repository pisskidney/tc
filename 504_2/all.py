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
                seq = seq[:i+1] + seq[-1:-(n-i):-1]
            else:
                ans += 1
                seq = seq[:i+1] + ''.join(['W' if x == 'B' else 'B' for x in seq[i+1:]])
            i += 1
        return ans


class MathContest2(object):
    def countBlack(self, seq, rep):
        seq = seq * rep
        n = len(seq)
        i = 0
        j = n - 1
        left = True
        ans = 0
        while i <= j:
            x = seq[i] if left else seq[j]
            if left:
                i += 1
            else:
                j -= 1

            if x == 'W':
                left = not left
            else:
                ans += 1
                seq = seq[0:i] + ''.join(['B' if x == 'W' else 'W' for x in seq[i:j+1]]) + seq[j+1:n]
        return ans


class MathContest3(object):
    def countBlack(self, seq, rep):
        if seq == 'W':
            return 0
        if seq == 'B':
            return 1
        seq = seq * rep
        n = len(seq)
        i = 0
        j = n - 1
        left = True
        inv = False
        ans = 0
        while i <= j:
            x = seq[i] if left else seq[j]

            if left:
                i += 1
            else:
                j -= 1

            if (x == 'W' and not inv) or (x == 'B' and inv):
                left = not left
            else:
                inv = not inv
                ans += 1
        return ans
