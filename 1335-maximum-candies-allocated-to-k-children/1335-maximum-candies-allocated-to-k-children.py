class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort()
        l, r = 1, candies[-1]
        result = 0

        while (l <= r):
            mid = (l + r) // 2
            total = sum([candy // mid for candy in candies])
            if total >= k:
                l = mid + 1
                result = max(result, mid)
            else:
                r = mid - 1
        return result