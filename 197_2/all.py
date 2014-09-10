#!/usr/bin/python


class GardenHose(object):
    def countDead(self, n, row, col, hose):
        dead = 0
        for i in range(n):
            for j in range(n):
                if (
                    (i + 1) * col > hose and (j + 1) * row > hose and
                    (i - n + 1) * col > hose and (j - n + 1) * row > hose
                ):
                    dead += 1
        return dead


class GeneralChess(object):
    def getAttacks(self, i):
        cords = []
        ones = (-1, 1)
        twos = (-2, 2)
        for o in ones:
            for t in twos:
                cords.append((o + i[0], t + i[1]))
                cords.append((t + i[0], o + i[1]))
        return cords


    def attackPositions(self, pieces):
        pieces = tuple((int(x.split(',')[0]), int(x.split(',')[1])) for x in pieces)
        coords = self.getAttacks(pieces[0])
        for i in pieces[1:]:
            c = self.getAttacks(i)
            to_del = []
            for j in coords:
                if j not in c:
                    to_del.append(j)
            for x in to_del:
                coords.remove(x)
        return ["%s,%s" % (x, y) for x, y in sorted(coords, key=lambda x: x[0])]

    
print GeneralChess().attackPositions(["2,1", "-1,-2"])
