class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        start = 0
        curr = nums[0]
        if curr >= target:
            return 1
        for end in range(1, len(nums)):
            curr += nums[end]
            while curr >= target:
                ans = min(ans, end-start+1)
                curr -= nums[start]
                start += 1
        if ans == float('inf'):
            ans = 0
        return ans
            