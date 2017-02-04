#!/usr/bin/python


class SellingFruits:
    def maxDays(self, x, f, d, p):
        cost_life = x
        fruits = f
        dollars = d
        cost_fruit = p
        res = 0
        res = min(dollars / cost_life, fruits)
        if dollars / cost_life <= fruits:
            return res
        dollars -= cost_life * res
        return res + dollars / (cost_fruit + cost_life)


class ThreeIncreasing:
    def minEaten(self, a, b, c):
        res = 0
        if b >= c:
            res = b - c + 1
            b -= (b - c + 1)
        if a >= b:
            res += a - b + 1
            a -= (a - b + 1)
        if a < 1 or b < 1 or c < 1:
            return -1
        return res


class MappingABC2:
    def countStrings(self, t):
        if len(set(t)) < 3:
            return 0
        nrs = len(set(t))
        visited = []
        res = 0
        h = {x: 3 for x in set(t)}
        for i in xrange(len(t)):
            for j in xrange(i + 1, len(t)):
                for k in xrange(j + 1, len(t)):
                    if t[i] != t[j] and t[j] != t[k] and t[i] != t[k] and [t[i], t[j], t[k]]:
                        toadd = 1
                        c = dict(h)
                        c[t[i]], c[t[j]], c[t[k]] = 1, 1, 1
                        visited = {}
                        abc = {t[i]: 1, t[j]: 1, t[k]: 1}
                        for z in xrange(i):
                            if t[z] != t[i]:
                                if t[z] not in visited and t[z] not in abc:
                                    c[t[z]] -= 1
                                    visited[t[z]] = 1
                            else:
                                c[t[z]] = 0
                        visited = {}
                        for z in xrange(i+1, j):
                            if t[z] != t[j]:
                                if t[z] not in visited and t[z] not in abc:
                                    c[t[z]] -= 1
                                    visited[t[z]] = 1
                            else:
                                c[t[z]] = 0
                        visited = {}
                        for z in xrange(j+1, k):
                            if t[z] != t[k]:
                                if t[z] not in visited and t[z] not in abc:
                                    c[t[z]] -= 1
                                    visited[t[z]] = 1
                            else:
                                c[t[z]] = 0
                        for prod in c.values():
                            toadd *= prod
                        res += toadd
        return res % (1000 * 1000 * 1000 + 7)


s = MappingABC2()
print s.countStrings((7,50,1,50,1,50,1,10,7))

        
