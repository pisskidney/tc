#!/usr/bin/python
import collections


class Egalitarianism3Easy(object):
    MAX = 999999
    def maxCities(self, n, a, b, lens):
        if n < 3:
            return n
        
        adj = [[self.MAX for i in range(n)] for i in range(n)]

        for i in range(0, len(a)):
            adj[a[i] - 1][b[i] - 1] = lens[i]

        for k in range(n):
            for i in range(n):
                for j in range(i + 1, n):
                    b = adj[k][i] + adj[k][j]
                    if adj[i][j] > b and i != j:
                        adj[i][j] = b

        res = collections.defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                if adj[i][j] != self.MAX:
                    res[adj[i][j]] += 1

        for i in range(n):
                print adj[i]
        print res
                
        return res[sorted(res, key=lambda x: res[x], reverse=True)[0]]


ee = Egalitarianism3Easy()
print ee.maxCities(10, (1,1,1,1,1,1,1,1,1), (2,3,4,5,6,7,8,9,10), (1000,1000,1000,1000,1000,1000,1000,1000,1000))
