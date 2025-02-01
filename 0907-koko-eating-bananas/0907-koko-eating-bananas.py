import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        end = max(piles)
        start = max(1, sum(piles) // h)
        ans = end
        while start <= end:
            mid = (start + end) // 2
            eath = sum([math.ceil(i / mid) for i in piles])
            if eath > h:
                start = mid + 1
            elif eath <= h:
                ans = mid
                end = mid - 1
        return ans

            