#!/usr/bin/python

class TheAlmostLuckyNumbersDivTwo(object):
    def find(self, a, b):
        ans = 0
        for x in range(a, b+1):
            f = str(x)
            c = f.count('4') + f.count('7')
            if len(f) - c <= 1:
                ans += 1
        return ans


class TheLuckyGameDivTwo:
    def find(self, a, b, jlen, blen):
        v = list()
        v.append(0)
        for i in xrange(1, b + 1):
            f = str(i)
            c = f.count('4') + f.count('7')
            t = 0 if len(f) != c else 1
            v.append(v[i-1] + t)
        maxx = 0
        for i in xrange(a, b - jlen + 2):
            minn =  100
            for j in xrange(i, i + jlen - blen + 1):
                minn = min(minn, v[j + blen - 1] - v[j - 1])
            maxx = max(maxx, minn)
        return maxx


#print TheLuckyGameDivTwo().find(4, 8, 3, 2)
#print '-' * 100
#print TheLuckyGameDivTwo().find(1, 100, 100, 100)
print TheLuckyGameDivTwo().find(1, 4747, 2825, 99)
                

            
