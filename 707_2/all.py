#!/usr/bin/python


class StepsConstruct:
    def construct(self, board, k):
        if board[0][0] == '#':
            return ''
        from collections import deque, defaultdict
        visited = {(0, 0): True}
        paths = defaultdict(list)
        q = deque([(0, 0)])
        best = None
        end = (len(board)-1, len(board[0])-1)
        c = 0
        moves = {(-1, 0) : ['U'], (1, 0) : ['D'], (0, 1): ['R'], (0, -1): ['L']}
        while q:
            c += 1
            node = q.popleft()
            if node == end:
                best = paths[node]
                break
            x, y = node
            for move in moves:
                potential = x + move[0], y + move[1]
                if (0 <= potential[0] < len(board) and
                    0 <= potential[1] < len(board[0]) and
                    potential not in visited and 
                    board[potential[0]][potential[1]] == '.'):
                        visited[potential] = True
                        q.append(potential)
                        paths[potential] = paths[node] + moves[move]
        if best is None:
            return ''
        path_len = len(best)
        if k < path_len:
            return ''
        if k == path_len:
            return ''.join(best)
        if k % 2 != path_len % 2:
            return ''
        counter = ['U'] if best[0] == 'D' else ['L']
        best = [best[0]] + ((counter + [best[0]]) * ((k - path_len) / 2)) + best[1:]
        return ''.join(best)


class Cross:
    def exist(self, board):
        for i in xrange(1, len(board) - 1):
            for j in xrange(1, len(board[0]) - 1):
                if board[i][j] == board[i-1][j] == board[i+1][j] == board[i][j-1] == board[i][j+1] == '#':
                    return 'Exist'
        return 'Does not exist'


c = Cross()
b = ["........", "#.#.....", "..##....", "........", "#..#....", ".......#",
"........", "........", "........", "........", "........", ".......#",
"........", "........", "....#...", "......#.", "........", "........",
"........", "....#...", "......#.", "........", "........", "........",
"...#...."]
print c.exist(b)
print '-' * 20


sc = StepsConstruct()
board = [".......", ".#.....", ".......", "..#....", ".......", ".##....",
".......", "....#..", "...#...", ".....#.", ".#.....", ".#.....", ".......",
".......", ".......", ".......", "#......", "....#..", ".......", ".......",
".......", "....#..", ".......", ".#.....", ".......", ".......", "#..#...",
"...#...", "......#", "#......", ".......", ".......", ".......", "...#...",
".......", ".....#.", ".......", "......#", ".#.....", ".......", ".......",
"...#...", ".......", ".#.....", ".......", "..#...."]
print len(board)
print sc.construct(board, 1461)




