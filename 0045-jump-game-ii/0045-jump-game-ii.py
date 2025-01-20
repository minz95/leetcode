class Solution:
    def jump(self, nums: List[int]) -> int:
        current_end = 0
        farthest = 0
        count = 0

        for i in range(0, len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                current_end = farthest
                count += 1
        return count
                