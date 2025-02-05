from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for n in graph[course]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)
        return taken == numCourses
