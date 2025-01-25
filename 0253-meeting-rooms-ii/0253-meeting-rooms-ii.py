import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        now = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(now, intervals[0][1])
        max_count = 1

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            while now and s >= now[0]:
                heapq.heappop(now)
            heapq.heappush(now, e)
            max_count = max(max_count, len(now))
        return max_count
                