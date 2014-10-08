#!/usr/bin/python


class ImportantTasks():
    def maximalCost(self, c, co):
        c = list(c)
        n = 0
        co = list(co)
        while c and co:
            maxc = max(c)
            maxco = max(co)
            if maxco >= maxc:
                co.remove(maxco)
                n += 1
            c.remove(maxc)
        return n


dx = (-1, -1, 1, 1, 2, 2, -2, -2)
dy = (-2, 2, 2, -2, -1, 1, -1, 1)


class KnightsTour():
    def access(self, b, pos):
        res = []
        for i in xrange(len(dx)):
            newx = pos[0] + dx[i]
            newy = pos[1] + dy[i]
            if (
                newx >= 0 and newx < 8 and newy >= 0 and newy < 8
                and b[newx][newy] != -1
            ):
                res.append((newx, newy))
        return res

    def visitedPositions(self, board):
        b = [[0 for _ in xrange(len(board))] for _ in xrange(len(board))]
        pos = (0, 0)
        c = 1

        for i in xrange(len(board)):
            for j in xrange(len(board)):
                if board[i][j] == '*':
                    b[i][j] = -1
                elif board[i][j] == 'K':
                    pos = (i, j)
                    b[i][j] = -1

        while True:
            newpos = self.access(b, pos)
            if not newpos:
                break
            minacs = 9
            minpos = (0, 0)
            for i in xrange(len(newpos)):
                ac = len(self.access(b, (newpos[i][0], newpos[i][1])))
                if (
                    ac < minacs or
                    (
                        ac == minacs and
                        (
                            newpos[i][0] < minpos[0]
                            or newpos[i][0] == minpos[0]
                            and newpos[i][1] < minpos[1]
                        )
                    )
                ):
                    minpos = (newpos[i][0], newpos[i][1])
                    minacs = ac
            b[minpos[0]][minpos[1]] = -1
            pos = minpos

            c += 1

        return c
