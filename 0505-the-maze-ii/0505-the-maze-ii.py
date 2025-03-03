from collections import deque
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = [[float('inf')] * n for _ in range(m)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(start, 0)])
        visited[start[0]][start[1]] = 1
        dist_min = -1

        while q:
            (x, y), dist = q.popleft()
            if x == destination[0] and y == destination[1]:
                dist_min = dist if dist_min == -1 else min(dist_min, dist)
                continue
            for dx, dy in moves:
                nx, ny = x, y
                d = 0
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx+dx][ny+dy] == 0:
                    nx += dx
                    ny += dy
                    d += 1
                if dist + d < visited[nx][ny]:
                    q.append(((nx, ny), dist + d))
                    visited[nx][ny] = dist + d
        return dist_min