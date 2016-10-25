#!/usr/bin/python


class Initials:
    def getInitials(self, name):
        return [x[0] for x in name.split()]


class RepeatStringEasy:
    def maximalLength(self, s):
        if len(set(s)) == len(s):
            return 0
        if len(s) == 2:
            return 2
        res = 0
        for x in xrange(1, len(s) - 1):
            nrs = [[] for _ in s]
            for i in xrange(x, len(s)):
                for j in xrange(0, x):
                    if s[i] == s[j]:
                        nrs[i].append(j)
            nrs = [x for x in nrs if x]
            if not nrs:
                continue
            dp = [[1 for _ in x] for x in nrs]
            for i in xrange(1, len(nrs)):
                for j in xrange(i):
                    for k in xrange(len(nrs[i])):
                        for l in xrange(len(nrs[j])):
                            if nrs[i][k] > nrs[j][l] and dp[i][k] < dp[j][l] + 1:
                                dp[i][k] = dp[j][l] + 1
            lens = [aa for bb in dp for aa in bb]
            if max(lens) > res: res = max(lens)
        return res * 2

r = RepeatStringEasy()
#print r.maximalLength('aababbababbabbbbabbabb')
print r.maximalLength('kk')


                
            
















class RepeatStringEasyOld:
    def maximalLength(self, s):
        n = len(s)
        if n < 2:
            return 0
        if len(set(s)) == n:
            return 0
        res = 0
        for i in xrange(1, n):
            for j in xrange(i):
                local = 0
                fromm = i
                for k in xrange(j, i):
                    for p in xrange(fromm, n):
                        if s[k] == s[p]:
                            local += 2
                            fromm = p+1
                            break
                if local > res:
                    res = local
        return res


i = Initials()
print i.getInitials('laugh out loud')
