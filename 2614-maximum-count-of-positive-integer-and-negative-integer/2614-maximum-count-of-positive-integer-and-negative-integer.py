class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        zero = 0
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            elif n > 0:
                return max(i-zero, len(nums)-i)
        return len(nums)-zero