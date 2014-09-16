#!/usr/bin/python


class SRMCards(object):
    def maxTurns(self, srms):
        i = 0
        c = 0
        srms = sorted(srms)
        while i < len(srms):
            if i != len(srms) - 1 and srms[i+1] == srms[i] + 1:
                c += 1
                i += 2
            else:
                c += 1
                i += 1
        return c


class MafiaGame(object):
    def vote(self, h, decs):
        to_vote = 0
        c = 1
        for i in range(len(decs)):
            if decs[i] in h:
                h[decs[i]] += 1
            else:
                to_vote += 1
        for _ in range(to_vote):
            m = sorted(h, key=lambda x: h[x])[0]
            c = h.values().count(m)
            h[m] += 1

        maxx = sorted(h, key=lambda x: h[x])[-1]
        to_del = []
        for i in h:
            if h[i] != h[maxx]:
                to_del.append(i)
        for x in to_del:
            del h[x]
        print h
        return c

    def probabilityToLose(self, n, decs):
        probs = {x: 0 for x in range(n)}

        old = len(probs)
        while True: 
            c = self.vote(probs, decs)
            new = len(probs)
            if len(probs) == 1:
                return 1.0/c
            if old == new:
                return 0.0
            old = new

        return 1.0/c

#print MafiaGame().probabilityToLose(3, (1, 1, 1))
#print MafiaGame().probabilityToLose(5, (1, 2, 3))
print MafiaGame().probabilityToLose(20, (1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 18, 19, 0))
