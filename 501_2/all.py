#!/usr/bin/python


class FoxProgression(object):
    def theCount(self, p):
        if len(p) == 1:
            return -1
        a = p[1] - p[0]
        g = float(p[1])/p[0]
        na, ng = p[1]+a, p[1]*g
        for i in range(2, len(p)):
            if p[i] - p[i - 1] != a:
                a = -1
                na = p[i] + a
            if float(p[i])/p[i - 1] != g:
                g = -1
                ng = p[i] * g
        print a, g
        if g != -1 and int(g) != g:
            g = -1
        if a == -1 and g == -1:
            return 0
        elif g == -1 or a == -1:
            return 1
        elif int(na) == int(ng):
            return 1
        else:
            return 2
            

class FoxPlayingGame(object):
    def theMax(self, na, nb, pa, pb):
        pa = pa / 1000.0
        pb = pb / 1000.0
        if min(na, nb) == 0:
            return na*pa*pb**nb
        c = 0
        if pa > 0:
            if pb > 1:
                return na*pa*pb**nb
            elif pb < 1 and pb >= 0:
                return na*pa
            else:
                if nb % 2:
                    nb -= 1
                return na*pa*pb**nb
        else:
            if pb > 1:
                return na*pa
            elif pb < 1 and pb >= 0:
                return na*pa*pb**nb
            else:
                if not nb % 2:
                    nb -= 1
                return na*pa*pb**nb
        return None
