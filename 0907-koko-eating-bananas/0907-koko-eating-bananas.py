import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        end = max(piles)
        start = max(1, sum(piles) // h)
        while start < end:
            mid = (start + end) // 2
            eath = sum([math.ceil(i / mid) for i in piles])
            if eath > h:
                start = mid+1
            else:
                end = mid
        return start

            