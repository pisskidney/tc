#!/usr/bin/python


class Arrfix:
    def mindiff(self, A, B, F):
        from collections import defaultdict
        fs = defaultdict(int)
        goods = defaultdict(int)
        for f in F:
            fs[f] += 1
        diffs = []
        for i in xrange(len(A)):
            if A[i] != B[i]:
                diffs.append(B[i])
            else:
                goods[A[i]] += 1

        for k in fs:
            while fs[k] > 0 and k in diffs:
                fs[k] -= 1
                diffs.remove(k)
        if sum(fs.values()) > 0:
            for k, v in fs.iteritems():
                if v > 0 and k in goods:
                    fs[k] -= min(fs[k], goods[k])
        return max(sum(fs.values()), len(diffs))


s = Arrfix()
print s.mindiff([1, 1, 1], [2, 2, 2], [2])


class Ropestring:
    def makerope(self, s):
        even, odd = [], []
        counting = False
        c, dots = 0, 0
        if '-' not in s:
            return s
        for i in xrange(0, len(s)):
            if s[i] == '-':
                if not counting:
                    counting = True
                    c = 0
                c += 1
            else:
                if counting:
                    counting = False
                    if c % 2 == 0:
                        even.append(c)
                    else:
                        odd.append(c)
                dots += 1
        if counting:
            if c % 2 == 0:
                even.append(c)
            else:
                odd.append(c)

        even, odd = sorted(even, reverse=True), sorted(odd, reverse=True)
        res = '.'.join(['-' * k for k in even])
        if odd and even:
            res += '.'
        res += '.'.join(['-' * k for k in odd])
        res += '.' * (dots - (len(even) + len(odd) - 1))
        return res


s = Ropestring()
print s.makerope('....')
