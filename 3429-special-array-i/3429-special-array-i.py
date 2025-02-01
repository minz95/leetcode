class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        curr = nums[1] % 2
        if nums[0] % 2 == curr:
            return False
        for i in range(2, len(nums)):
            if nums[i] % 2 == curr:
                return False
            curr = nums[i] % 2
        return True
