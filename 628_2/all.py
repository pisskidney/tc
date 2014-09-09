#!/usr/bin/python


class BishopMove(object):
    def howManyMoves(self, i, j, p, q):
        if (i == p) and (j == q):
            return 0
        elif (i + j) % 2 != (p + q) % 2:
            return -1
        elif abs(i - p) == abs(j - q):
            return 1
        else:
            return 2


class BracketExpressions(object):
    inv = {'(': ')', '[': ']', '{': '}'}

    def removeX(self, d):
        for i in range(len(d)):
            if d[i] in ('(', '[', '{') and d[i + 1] == 'X' and i + 1 < len(d):
                del d[i + 1]
                del d[i]
                return True
        return False


    def ifPossible(self, s):
        d = list()
        for c in s:
            if c in ('(', '[', '{'):
                d.append(c)
            elif c in (')', ']', '}'):
                if d[-1] == 'X' or self.inv[d[-1]] == c:
                    d.pop()
                else:
                    return 'impossible'
            elif c == 'X':
                d.append(c)

        while (self.removeX(d)):
            self.removeX(d)

        if d and d.count('X') == len(d):
            if d.count('X') % 2:
                return 'impossible'
            else:
                return 'possible'
            
        return 'possible' if not bool(d) else 'impossible'


def main():
    bm = BishopMove()
    print bm.howManyMoves(4, 0, 0, 0)

    be = BracketExpressions()
    print be.ifPossible('([]X()[()]XX}[])X{{}}]')


if __name__ == "__main__":
    main()
