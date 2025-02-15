from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def check(board):
            if board[0][0] == 1 and board[0][1] == 2 and board[0][2] == 3 and \
                board[1][0] == 4 and board[1][1] == 5 and board[1][2] == 0:
                return True
            return False
        def hash(board):
            s = ""
            for i in range(2):
                for j in range(3):
                    s += str(board[i][j])
            return s

        if check(board):
            return 0
        visited = set(hash(board))
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        zero = (-1, -1)
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    zero = (i, j)
                    break
        q = deque([])
        for dx, dy in moves:
            nx, ny = zero[0] + dx, zero[1] + dy
            if 0 <= nx < 2 and 0 <= ny < 3:
                q.append((zero, (nx, ny), [row[:] for row in board], 1))

        while q:
            z, (i, j), b, cnt = q.popleft()
            # print(z[0], z[1], i, j, b, cnt)
            prev = b[i][j]
            b[i][j] = b[z[0]][z[1]]
            b[z[0]][z[1]] = prev
            if hash(b) in visited:
                continue
            visited.add(hash(b))
            if check(b):
                return cnt
            
            for dx, dy in moves:
                nx, ny = i + dx, j + dy
                if 0 <= nx < 2 and 0 <= ny < 3:
                    q.append(((i, j), (nx, ny), [row[:] for row in b], cnt+1))
        return -1
                