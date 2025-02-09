class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        diff = {}

        for i in range(len(nums)):
            d = i - nums[i]
            c = diff.get(d, 0)
            count += i - c
            diff[d] = c + 1
        return count