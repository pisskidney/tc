#!/usr/bin/python


class NamingConvention():
    def toCamelCase(self, var):
        words = var.split('_')
        for i in xrange(1, len(words)):
            words[i] = words[i].capitalize()
        return ''.join(words)


class NarrowPassage2Easy2():
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
        print visited
        return c


class NarrowPassage2Easy():
    def count(self, arr, max_):
        n=[1]*len(arr)
        prev=arr[0]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]+arr[i]<=max_:
                    n[i-1]=n[i-1]+1
                else:
                    break
        q = 1
        for i in n:
            q=q*i
        return q

print NarrowPassage2Easy().count((1,2,3,1,1,1), 42)
