#!/usr/bin/python


'''
There is a rectangular hole in the ground. You are given the dimensions of this
rectangle: integers holeH and holeW.  You have a rectangular board. You are
given its dimensions: integers boardH and boardW. You would like to use the
board to cover the hole.  There are some rules you must follow when covering
the hole: You may rotate the board, but you must place it so that the sides of
the board are parallel to the sides of the hole.  The board must cover the
entire hole.  All corners of the board must be strictly outside the hole. (That
is, they are not allowed to lie on the boundary of the hole.) If you can cover
the hole using the board you have, return 1. Otherwise, return -1.
'''


class RectangleCoveringEasy(object):
    def solve(self, holeH, holeW, boardH, boardW):
        if (
            (holeH < boardH and holeW <= boardW) or
            (holeH <= boardH and holeW < boardW)
        ) or (
            (holeH < boardW and holeW <= boardH) or
            (holeH <= boardW and holeW < boardH)
        ):
            return 1
        return -1


def main():
    hh = input('holeH=')
    hw = input('holeW=')
    bh = input('holeH=')
    bw = input('holeW=')
    rce = RectangleCoveringEasy()
    print rce.solve(hh, hw, bh, bw)


if __name__ == "__main__":
    main()
