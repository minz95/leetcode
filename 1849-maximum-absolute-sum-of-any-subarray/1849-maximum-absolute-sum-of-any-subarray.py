class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_sum = 0
        max_sum = 0
        result = -float('inf')

        for n in nums:
            prefix_sum += n
            result = max(abs(prefix_sum-min_sum), abs(prefix_sum-max_sum), result)
            min_sum = min(min_sum, prefix_sum)
            max_sum = max(max_sum, prefix_sum)
        return result