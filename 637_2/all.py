#!/usr/bin/python


class GreaterGameDiv2():
    def calc(self, snuke, sothe):
        c = 0
        for i in xrange(len(snuke)):
            if snuke[i] > soethe:
                c += 1
        return c

class PathGameDiv2():
    def calc(self, b):
        row1 = b[0].find('#')
        row2 = b[1].find('#')
        row = 0
        if (row2 > row1 or row2 == -1) and row1 != -1:
            row = 1
        print row
        c = 0
        inv = {0: 1, 1: 0}
        col = 0
        while col <= len(b[0]) - 1:
            if col + 1 < len(b[0]) and b[row][col+1] == '#':
                row = inv[row]
            elif b[inv[row]][col] == '.':
                c += 1

            col += 1
        return c
                
print PathGameDiv2().calc(('.', '#'))

