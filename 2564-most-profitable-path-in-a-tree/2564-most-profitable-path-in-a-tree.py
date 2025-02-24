from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        bob_time = [float('inf')] * n  # Bob의 각 노드 도착 시간 기록

        def find_bob_time(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True
            for nei in graph[node]:
                if nei != parent and find_bob_time(nei, node, time + 1):
                    bob_time[node] = time
                    return True
            return False

        find_bob_time(bob, -1, 0)
        max_profit = float('-inf')
        def dfs_alice(node, parent, time, profit):
            nonlocal max_profit

            if time < bob_time[node]:
                profit += amount[node] 
            elif time == bob_time[node]:
                profit += amount[node] // 2 

            if node != 0 and len(graph[node]) == 1:
                max_profit = max(max_profit, profit)
                return

            for nei in graph[node]:
                if nei != parent:
                    dfs_alice(nei, node, time + 1, profit)
            
        dfs_alice(0, -1, 0, 0)
        return max_profit