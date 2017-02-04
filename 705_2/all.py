#!/usr/bin/python


class AlphabetOrderDiv2:
    def is_start_vertex(self, i, adj):
        for row in xrange(len(adj)):
            if adj[row][i] == 1:
                return False
        return True


    def isOrdered(self, words):
        adj = [[0] * 26 for _ in xrange(26)]
        visited = [0] * 26
        letters = []
        for i in xrange(len(words)):
            for j in xrange(len(words[i])-1):
                if words[i][j] != words[i][j+1]:
                    adj[ord(words[i][j]) - ord('a')][ord(words[i][j+1]) - ord('a')] = 1
        processed = True
        while processed:
            processed = False
            for i in xrange(len(visited)):
                if visited[i] == 0 and self.is_start_vertex(i, adj):
                    visited[i] = 1
                    adj[i] = [0] * 26
                    processed = True
        return 'Possible' if 0 not in visited else 'Impossible'

s = AlphabetOrderDiv2()
print s.isOrdered(['ab', 'bc', 'cd',])


class SuperUserDo:
    def install(self, A, B):
        h = {}
        for i in xrange(len(A)):
            for j in xrange(A[i], B[i] + 1):
                h[j] = True
        res = 0
        for _ in h:
            res += 1
        return res
