from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(v % 2 == 0 for v in Counter(nums).values())