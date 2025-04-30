class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            s = str(n)
            if len(s) % 2 == 0:
                total += 1
        return total