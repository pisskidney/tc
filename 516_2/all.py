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
                
            
print NetworkXZeroOne().reconstruct('o??x??o')

