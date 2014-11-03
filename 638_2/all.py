#!/usr/bin/python


class NamingConvention():
    def toCamelCase(self, var):
        words = var.split('_')
        for i in xrange(1, len(words)):
            words[i] = words[i].capitalize()
        return ''.join(words)


class NarrowPassage2Easy():
    def count(self, size, maxsize):
        c = 1
        if len(size) == 1:
            return 1
        q = [tuple(range(len(size)))]
        visited = set([tuple(range(len(size)))])
        while q:
            cur = q.pop()
            for i in xrange(len(cur) - 1):
                if size[cur[i]] + size[cur[i+1]] <= maxsize:
                    new = cur[:i] + (cur[i+1],) + (cur[i],) + cur[i+2:]
                    if new not in visited:
                        visited.add(new)
                        q.append(new)
                        c += 1
        return c


print NarrowPassage2Easy().count((1,), 100)
