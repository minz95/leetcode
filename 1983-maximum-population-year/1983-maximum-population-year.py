import heapq
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop = []
        logs.sort(key = lambda x: x[0])

        maxcnt = 0
        year = logs[0][0]
        for i, l in enumerate(logs):
            b, d = l[0], l[1]
            heapq.heappush(pop, d)
            while pop and pop[0] <= b:
                heapq.heappop(pop)
            if maxcnt < len(pop):
                maxcnt = len(pop)
                year = b
        return year
