import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while nums[0] < k:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            n = a * 2 + b
            heapq.heappush(nums, n)
            count += 1
        return count

        