class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sizes = {}
        island = 2

        def dfs(r, c, island):
            stack = [(r, c)]
            grid[r][c] = island
            size = 0

            while stack:
                x, y = stack.pop()
                size += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = island
                        stack.append((nx, ny))
            return size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    sizes[island] = dfs(r, c, island)
                    island += 1
        max_island = max(sizes.values(), default=0)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    nsize = 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                            island_id = grid[nx][ny]
                            if island_id not in seen:
                                nsize += sizes[island_id]
                                seen.add(island_id)
                        max_island = max(max_island, nsize)
        return max_island