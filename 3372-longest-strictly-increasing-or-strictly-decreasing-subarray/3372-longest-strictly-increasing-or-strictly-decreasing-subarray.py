class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_len = 1
        curr = 1
        increasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if increasing:
                    curr += 1
                else:
                    increasing = True
                    curr = 2
            elif nums[i] < nums[i-1]:
                if increasing:
                    increasing = False
                    curr = 2
                else:
                    curr += 1
            else:
                curr = 1
            max_len = max(curr, max_len)
        return max_len
                
            