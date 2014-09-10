#!/usr/bin/python


class StringMult(object):
    def times(self, s, k):
        res = ""
        if not s or not k:
            return ""
        if k > 0:
            for i in range(k):
                res += s
        else:
            for i in range(abs(k)):
                res += s[::-1]

        return res


print StringMult().times("Racecar", -5)
