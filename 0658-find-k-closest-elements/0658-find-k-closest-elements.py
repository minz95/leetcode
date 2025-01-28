import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for i in range(0, len(arr)):
            heapq.heappush(h, (-abs(arr[i]-x), -i))
            if i >= k and h:
                heapq.heappop(h)
        result = []
        while h:
            result.append(arr[-heapq.heappop(h)[-1]])
        return sorted(result)