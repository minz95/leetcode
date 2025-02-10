class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        size = len(nums) - 3
        min_diff = float('inf')
        for i in range(len(nums)-size+1):
            diff = nums[i+size-1] - nums[i]
            min_diff = min(min_diff, diff)
            print(diff)
        return min_diff