import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = list(range(n))
        count = [0] * n
        meetings.sort(key=lambda x: x[0])
        now = []

        for s, e in meetings:
            while now and now[0][0] <= s:
                prev = heapq.heappop(now)
                heapq.heappush(rooms, prev[1])
            if rooms:
                num = heapq.heappop(rooms)
                heapq.heappush(now, (e, num))
                count[num] += 1
            else:
                pe, rn = heapq.heappop(now)
                pe += e - s
                heapq.heappush(now, (pe, rn))
                count[rn] += 1

        return count.index(max(count))
            