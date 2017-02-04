#!/usr/bin/python


class AlternatingString:
    def maxLength(self, s):
        res = 1
        count = 1
        for i in xrange(1, len(s)):
            if s[i] != s[i-1]:
                count += 1
            else:
                res = max(count, res)
                count = 1
        return max(res, count)
