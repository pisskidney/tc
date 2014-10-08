#!/usr/bin/python


class SoldierLabeling():
    def count(self, n, l, u):
        low = 10**(l-1)
        up = 10**l
        if n < up:
            up = n + 1
        return up - low


class CubeWalking:
    def finalPosition(self, m):
        rot = 0
        pos = (1, 1)
        for mv in m:
            if mv == 'L':
                rot += 3
            elif mv == 'R':
                rot += 1
            else:
                if rot % 4 == 0:
                    pos = (pos[0] - 1, pos[1])
                elif rot % 4 == 1:
                    pos = (pos[0], pos[1] + 1)
                elif rot % 4 == 2:
                    pos = (pos[0] + 1, pos[1])
                elif rot % 4 == 3:
                    pos = (pos[0], pos[1] - 1)
                if pos[0] == -1:
                    pos = (2, pos[1])
                elif pos[0] == 3:
                    pos = (0, pos[1])
                if pos[1] == -1:
                    pos = (pos[0], 2)
                elif pos[1] == 3:
                    pos = (pos[0], 0)
        if pos == (1, 1):
            return 'GREEN'
        elif pos in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            return 'BLUE'
        else:
            return 'RED'


print CubeWalking().finalPosition('WWLLWRWLWLLRWW')
