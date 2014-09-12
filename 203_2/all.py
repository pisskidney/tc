#!/usr/bin/python


class UserName(object):
    def newMember(self, ex, n):
        if n not in ex:
            return n
        for i in range(1, 100):
            if n + str(i) not in ex:
                return n + str(i)


class MatchMaking(object):
    def dif(self, a, b):
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
        return c

    def makeMatch(self, women, awomen, men, amen, who):
        answ = dict()
        ansm = dict()
        for i in range(len(women)):
            answ[women[i]] = awomen[i]
            ansm[men[i]] = amen[i]
        women = sorted(women)
        men = sorted(men)
        while women:
            w = women[0]
            mindiff = len(awomen) + 1
            minman = None
            for m in men:
                d = self.dif(answ[w], ansm[m])
                if d < mindiff:
                    mindiff = d
                    minman = m
            if who == w:
                return minman
            else:
                women.remove(w)
                men.remove(minman)
        return None


class UnLinker(object):
    def valid(self, t):
        if not t:
            return False
        for c in t:
            if c in (' ', ',', ':', '/'):
                return False
        return True

    def clean(self, t):
        c = 1
        found = True
        pre = ('http://', 'http://www.', 'www.')
        suf = ('.org', '.com', '.edu', '.info', '.tv')
        fromm = 0
        while found:
            found = False
            fminl, fmaxl = 0, 0

            fmin = len(t) + 1
            for p in pre:
                x = t.find(p, fromm)
                if x >= 0 and x < fmin:
                    fmin = x
                    fminl = len(p)
            fromm = fmin + 1

            fmax = -1

            for s in suf:
                to = len(t)
                while t.rfind(s, fmin, to) != -1:
                    x = t.rfind(s, fmin, to)
                    if x >= 0 and x > fmax and self.valid(t[fmin+fminl:x]):
                        fmax = x
                        fmaxl = len(s)
                        found = True
                        break
                    else:
                        to = x - 1

            if fmin == -1:
                return t

            if fmin != -1 and fmax != -1:
                t = t[:fmin] + 'OMIT' + str(c) + t[fmax + fmaxl:]
                c += 1
        return t


print 'http.//say.org,www.jeeves.x.info,www.comhttp://.tv'
print UnLinker().clean('http.//say.org,www.jeeves.x.info,www.comhttp://.tv')


