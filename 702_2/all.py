#!/usr/bin/python


class SubsetSumExtreme:
    def getExpectation(self, block, face):
        return self.bfs(block, face)

    def getBlock(self, block, i):
        if not block:
            return [], False, 0
        if i < max(block) or i > sum(block):
            return [], False, sum(block)
        best, found = 0, False
        for j in xrange(2**len(block)):
            summ = 0
            for k in xrange(len(block)):
                if (1 << k) & j:
                    summ += block[k]
            if summ == i and bin(i).count('1') > bin(best).count('1'):
                found = True
                best = i
        if found:
            newblock = block[:]
            toremove = []
            for k in xrange(len(block)):
                if (1 << k) & best:
                    toremove.append(block[k])
            for x in toremove:
                newblock.remove(x)
            return newblock, True, 0
        return [], False, sum(block)

    def bfs(self, block, face):
        x = []
        for i in xrange(len(face)):
            x.append(self.getBlock(block, face[i]))
        summ = 0
        for newblock, possible, res in x:
            if possible:
                summ += self.bfs(newblock, face)
            else:
                summ += res
        return float(summ) / len(face)

            
class GridSort():
    def sort(self, n, m, grid):
        yes, no = 'Possible', 'Impossible'
        if n == 1:
            return yes
        row, col = {}, {}
        for i in xrange(n):
            for j in xrange(m):
                cur = (grid[i*m+j] - 1) / m
                if cur in row:
                    if row[cur] != i:
                        print i, j
                        print cur
                        return no
                else:
                    row[cur] = i
                cur2 = (grid[i*m+j] - 1) % m
                if cur2 in col:
                    if col[cur2] != j:
                        return no
                else:
                    col[cur2] = j
        return yes


s = GridSort()
print s.sort(1, 1, [1])


class TestTaking():
    def findMax(self, questions, guessed, actual):
        t = actual
        f = questions - actual
        gt = guessed
        gf = questions - guessed
        return min(t, gt) + min(f, gf)


