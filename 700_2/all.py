#!/usr/bin/python


class Xylophone:
    def countKeys(self, keys):
        h = {}
        res = 0
        for k in keys:
            if k % 7 not in h:
                h[k%7] = 1
                res += 1
        return res


class XMarksTheSpot:
    def countArea(self, board):
        TT, LL = 55, 55
        BB, RR = -1, -1
        qs = []
        res = 0
        op = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '?':
                    qs.append((i, j))
                elif board[i][j] == 'O':
                    if i < TT: TT = i
                    if i > BB: BB = i
                    if j < LL: LL = j
                    if j > RR: RR = j
        k = len(qs)
        if not k:
            return (BB-TT+1)*(RR-LL+1)
        for perm in xrange(2**k):
            T, B, L, R = TT, BB, LL, RR
            for shift in xrange(k):
                op += 1
                if (1 << shift) & perm:
                    oi, oj = qs[k-shift-1][0], qs[k-shift-1][1]
                    if oi < T:
                        T = oi
                    if oi > B:
                        B = oi
                    if oj < L:
                        L = oj
                    if oj > R:
                        R = oj
            res += (B-T+1)*(R-L+1)
        return res


class XMarksTheSpot:
    def countArea(self, board):
        from itertools import combinations
        TT, LL = 55, 55
        BB, RR = -1, -1
        qs = []
        op = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '?':
                    qs.append((i, j))
                elif board[i][j] == 'O':
                    if i < TT: TT = i
                    if i > BB: BB = i
                    if j < LL: LL = j
                    if j > RR: RR = j
        res = (BB-TT+1)*(RR-LL+1)
        for k in xrange(1, len(qs) + 1):
            for perm in combinations(qs, k):
                for p in perm:
                    op += 1
                    T, B, L, R = TT, BB, LL, RR
                    op += 1
                    oi, oj = p[0], p[1]
                    if oi < T:
                        T = oi
                    if oi > B:
                        B = oi
                    if oj < L:
                        L = oj
                    if oj > R:
                        R = oj
                res += (B-T+1)*(R-L+1)
        print 'op ', op
        return res


s = XMarksTheSpot()
print s.countArea(['?????????O??????????'])

