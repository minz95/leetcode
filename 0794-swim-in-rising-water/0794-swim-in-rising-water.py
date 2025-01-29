import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        hmax = 0

        while q:
            height, r, c = heapq.heappop(q)
            hmax = max(hmax, height)
            if (r, c) == (n-1, n-1):
                return hmax
            for i, j in moves:
                nr, nc = r + i, c + j
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(q, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
