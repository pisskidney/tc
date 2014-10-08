#!/usr/bin/python


class TheEncryptionDivTwo():
    def encrypt(self, m):
        d = [x for x in xrange(ord('a'), ord('z') + 1)]
        e = {}
        ans = ''
        for x in m:
            if x in e:
                ans += chr(e[x])
            else:
                e[x] = d[0]
                d = d[1:]
                ans += e[x]
        return ans


class TheNewHouseDivTwo():
    def count(self, x, y):
        ans = []
        for i in xrange(len(x)):
            for j in xrange(i + 1, len(x)):
                if y[i] == y[j]:
                    for k in xrange(len(x)):
                        for l in xrange(k + 1, len(x)):
                            if (
                                x[k] == x[l] and
                                min(x[i], x[j]) < x[k] and
                                max(x[i], x[j]) > x[k] and
                                max(y[k], y[l]) > y[i] and
                                min(y[k], y[l]) < y[i]
                            ):
                                if (x[k], y[i]) not in ans:
                                    ans.append((x[k], y[i]))
        return len(ans)
