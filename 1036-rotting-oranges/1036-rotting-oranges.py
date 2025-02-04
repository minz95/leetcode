from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    count += 1
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        while q and count > 0:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in d:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        count -= 1
                        q.append((nx, ny))
        return time if count == 0 else -1
