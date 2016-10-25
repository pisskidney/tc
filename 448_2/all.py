#!/usr/bin/python


class TheBlackJackDivTwo():
    def score(self, cards):
        ans = 0
        for c in cards:
            if c[0] == 'A':
                ans += 11
            elif c[0] in [str(x) for x in xrange(2, 10)]:
                ans += int(c[0])
            else:
                ans += 10
        return ans


class TheCardShufflingDivTwo():
    def shuffle(self, n, m):
        cards = range(1, n + 1)
        n = len(cards)
        for k in xrange(n % m):

        return cards[0]

#print TheCardShufflingDivTwo().shuffle(5, 1)
print TheCardShufflingDivTwo().shuffle(998369, 967226)
