class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def dfs(visited, i, j, idx):
            if idx == len(word):
                return True
            d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in d:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in visited \
                    and board[nx][ny] == word[idx]:
                    visited.add((nx, ny))
                    result = dfs(visited, nx, ny, idx+1)
                    if result:
                        return True
                    visited.remove((nx, ny))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set([(i, j)])
                    if dfs(visited, i, j, 1):
                        return True
        return False
            