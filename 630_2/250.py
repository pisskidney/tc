#!/usr/bin/python


class DoubleLetter(object):
    def ableToSolve(self, S):
        s = list(S)
        removed = True
        while removed:
            removed = False
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    s.pop(i - 1)
                    s.pop(i - 1)
                    removed = True
                    break
        return len(s) == 0


dl = DoubleLetter()
print True, dl.ableToSolve('aabb')
print False, dl.ableToSolve('aabbc')
print False, dl.ableToSolve('aacbb')
print True, dl.ableToSolve('aabbcc')
print True, dl.ableToSolve('aa')

