#!/usr/bin/python


class AvoidRoads():
    def numWays(self, height, width, bad):
        dp = [[0 for _ in xrange(width+1)] for _ in xrange(height+1)]
        dp[0][0] = 1
        bad = [map(int, b.split()) for b in bad]
        for i in xrange(height+1):
            for j in xrange(width+1):
                if i == 0 and j == 0: continue;
                from_top = 0 if i - 1 < 0 or [i-1, j, i, j] in bad or [i, j, i-1, j] in bad else dp[i-1][j]
                from_left = 0 if j - 1 < 0 or [i, j-1, i, j] in bad or [i, j, i, j-1] in bad else dp[i][j-1]
                dp[i][j] = from_top + from_left
        return dp[height][width]


ar = AvoidRoads()

print ar.numWays(10, 100, ["0 2 0 3", "1 2 1 3", "2 2 2 3", "3 2 3 3", "4 2 4 3", "5 2 5 3", "6 2 6 3", "7 2 7 3", "8 2 8 3", "9 2 9 3"])



