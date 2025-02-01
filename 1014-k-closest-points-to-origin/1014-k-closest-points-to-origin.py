import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in range(len(points)):
            d = math.sqrt(pow(points[i][0], 2) + pow(points[i][1], 2))
            heapq.heappush(dist, (d, points[i]))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(dist)[1])
        return result
