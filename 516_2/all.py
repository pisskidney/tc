#!/usr/bin/python


class NetworkXZeroOne():
    def reconstruct(self, m):
        chars = list(m)
        while '?' in chars:
            for i in xrange(len(chars)):
                if chars[i] == '?':
                    if i - 1 >= 0 and chars[i - 1] in ('o', 'x'):
                        chars[i] = 'x' if chars[i - 1] == 'o' else 'o'
                    elif i + 1 < len(chars) and chars[i + 1] in ('o', 'x'):
                        chars[i] = 'x' if chars[i + 1] == 'o' else 'o'
        return ''.join(chars)
                

from collections import defaultdict
class NetworkXOneTimePad():
    def crack(self, p, c):
        res = 0
        keys = defaultdict(int)
        for i in xrange(len(p)):
            for j in xrange(len(c)):
                k = ''.join([str(int(p[i][q]) ^ int(c[j][q])) for q in xrange(len(p[0]))])
                keys[k] += 1
        for v in keys.values():
            if v == len(c):
                res += 1
        return res

print NetworkXOneTimePad().crack(
