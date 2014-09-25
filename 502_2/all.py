#!/usr/bin/python


class TheProgrammingContestDivTwo(object):
    def find(self, t, reqs):
        reqs = sorted(reqs)
        pen = []
        ttime = 0
        s = 0
        for x in reqs:
            pen.append(ttime + x)
            s += 1
            ttime += x
            if ttime > t:
                s -= 1
                return s, sum(pen[:-1])

        return s, sum(pen)


class TheLotteryBothDivs(object):
    def find(self, sufs):
        sufs = list(set(sufs))
        s = sufs[:]
        for i in range(len(sufs)):
            for j in range(i + 1, len(sufs)):
                if sufs[i].endswith(sufs[j]) and sufs[i] in s:
                    s.remove(sufs[i])
                elif sufs[j].endswith(sufs[i]) and sufs[j] in s:
                    s.remove(sufs[j])
        c = 0
        for x in s:
            c += 1.0 / (10**len(x))
        return c


#print TheLotteryBothDivs().find(("8542861", "1954", "6", "523", "000000000", "5426", "8"))
print TheLotteryBothDivs().find(("47", "58", "4747", "502"))
