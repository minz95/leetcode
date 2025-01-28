from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[0 for _ in range(n)] for _ in range(m)]
        max_fish = 0

        for i in range(0, m):
            for j in range(0, n):
                if visited[i][j] or grid[i][j] == 0:
                    continue
                fish_count = 0
                q = deque([(i, j)])
                while q:
                    ii, jj = q.popleft()
                    if visited[ii][jj]:
                        continue
                    fish_count += grid[ii][jj]
                    visited[ii][jj] = 1
                    for k in moves:
                        ni, nj = ii + k[0], jj + k[1]
                        if ni >= 0 and nj >= 0 and ni < m and nj < n and grid[ni][nj] > 0 \
                            and visited[ni][nj] == 0:
                            q.append((ni, nj))
                if fish_count > max_fish:
                    max_fish = fish_count

        return max_fish
