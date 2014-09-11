#!/usr/bin/python


class NoOrderOfOperations(object):
    def evaluate(self, s):
        ops = ('+', '-', '*')
        res = int(s[0])
        i = 1
        while i < len(s):
            if s[i] == '*':
                res *= int(s[i+1])
            elif s[i] == '+':
                res += int(s[i+1])
            else:
                res -= int(s[i+1])
            i += 2
        return res


class GravityBomb(object):
    def move(self, s):
        return move

    def aftermath(self, s):
        y = len(s[0])
        x = len(s)
        s = [['' + s[i][j] for j in range(y)] for i in range(x)]

        move = True
        while move:
            move = False
            if '.' not in s[-1]:
                s[-1] = ['.' for _ in range(len(s[0]))]
                move = True
            for i in range(len(s) - 2, -1, -1):
                for j in range(len(s[0])):
                    if s[i][j] == 'X' and s[i+1][j] == '.':
                        s[i][j] = '.'
                        s[i+1][j] = 'X'
                        move = True

        return [''.join(x) for x in s]
