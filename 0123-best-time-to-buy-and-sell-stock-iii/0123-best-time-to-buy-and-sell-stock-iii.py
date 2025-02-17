class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1, dp2, dp3, dp4 = float('-inf'), 0, float('-inf'), 0

        for p in prices:
            dp1 = max(dp1, -p)
            dp2 = max(dp2, dp1 + p)
            dp3 = max(dp3, dp2 - p)
            dp4 = max(dp4, dp3 + p)
        
        return dp4