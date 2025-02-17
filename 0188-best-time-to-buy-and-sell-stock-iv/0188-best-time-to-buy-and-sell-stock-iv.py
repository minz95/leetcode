class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0 for _ in range(k*2)]
        for i in range(k*2):
            if i % 2 == 0:
                dp[i] = float('-inf')
        for p in prices:
            for i in range(k*2):
                if i == 0:
                    dp[i] = max(dp[i], -p)
                elif i % 2 == 1:
                    dp[i] = max(dp[i], dp[i-1] + p)
                else:
                    dp[i] = max(dp[i], dp[i-1] - p)
        return dp[-1]