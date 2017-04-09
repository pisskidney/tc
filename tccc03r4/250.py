#!/usr/bin/python


class ChessMetric:
    def howMany(self, size, start, end, numMoves):
        dp = [[0 for _ in xrange(size)] for _ in xrange(size)]
        dp[start[0]][start[1]] = 1
        x = [-1,1,-1,1,0,0,1,-1,2,2,-2,-2,1,-1,1,-1]
        y = [-1,1,1,-1,1,-1,0,0,1,-1,1,-1,2,2,-2,-2]
        for _ in xrange(numMoves):
            dp2 = [[0 for _ in xrange(size)] for _ in xrange(size)]
            for i in xrange(size):
                for j in xrange(size):
                    for a, b in zip(x, y):
                        if i + a >= 0 and i + a < size and j + b >= 0 and j + b < size:
                            dp2[i][j] += dp[i+a][j+b]
            dp = dp2
        return dp[end[0]][end[1]]


cm = ChessMetric()
print cm.howMany(100, [0,0], [0,99], 50)
