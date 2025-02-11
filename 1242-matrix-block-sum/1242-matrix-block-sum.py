class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        
        for r in range(n):
            for c in range(m):
                for i in range(max(0, r-k), min(n, r+k+1)):
                    for j in range(max(0, c-k), min(m, c+k+1)):
                        ans[i][j] += mat[r][c]
        return ans