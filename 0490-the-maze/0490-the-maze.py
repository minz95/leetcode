from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[0] * n for _ in range(m)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([start])
        visited[start[0]][start[1]] = 1

        while q:
            x, y = q.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            
            for dx, dy in moves:
                nx, ny = x, y
                while dx != 0:
                    nx += dx
                    if nx < 0 or nx >= m or maze[nx][ny] == 1:
                        nx -= dx
                        dx = 0
                while dy != 0:
                    ny += dy
                    if ny < 0 or ny >= n or maze[nx][ny] == 1:
                        ny -= dy
                        dy = 0
                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
        return False
        