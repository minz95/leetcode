class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        d = [0] * (n * n + 1)
        for i in range(n*n):
            print(grid[i//n][i%n])
            d[grid[i//n][i%n]] += 1

        arr = [0, 0]
        for i in range(1, n*n+1):
            if d[i] == 2:
                arr[0] = i
            elif d[i] == 0:
                arr[1] = i
        return arr