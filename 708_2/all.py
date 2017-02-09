#!/usr/bin/python


class PalindromicSubseq2:
    def solve(self, s):
        from math import factorial as fact
        mod = 10**9 + 7
        a = [[] for x in xrange(26)]
        for i in xrange(len(s)):
            a[ord(s[i]) - 97].append(i)
        x = [1 for _ in xrange(len(s))]
        for i in xrange(1, len(s) - 1):
            score = 0
            finalscore = 0
            for j in xrange(len(a)):
                if a[j] and a[j][-1] > i and a[j][0] < i:
                    k = 0
                    while a[j][k] < i:
                        k += 1
                    score += min(k, len(a[j]) - k)
            for p in xrange(1, score + 1):
                scorefact = fact(score)
                finalscore += (scorefact / fact(score - p) * fact(p))
                if i == 2:
                    print (scorefact / fact(score - p) * fact(p)), 'x'
            if i == 3:
                print finalscore, score
            x[i] += finalscore
        return x


ps = PalindromicSubseq2()
print ps.solve('axbcba')


class SafeBetting:
    def minRounds(self, a, b, c):
        cash = b - a
        res = 0
        while cash + a < c:
            cash *= 2
            res += 1
        return res


class BuildingStrings:
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def build(self, i, j):
        res = self.abc[:i]
        while len(res) < j:
            res.append(res[0])
        return ''.join(res)

    def findAny(self, K):
        res = []
        newk = K
        maxstr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while len(maxstr) < 50:
            maxstr.append('a')
        maxstr = ''.join(maxstr)
        while newk >= 1300:
            res.append(maxstr)
            newk -= 1300
        if newk == 0:
            return res
        while newk > 0:
            for i in xrange(26, 0, -1):
                for j in xrange(49, i-1, -1):
                    if i * j <= newk:
                        print i, j
                        res.append(self.build(i, j))
                        newk -= i * j
        return res
