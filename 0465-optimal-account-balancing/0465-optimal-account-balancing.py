from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(int)
        for p1, p2, amount in transactions:
            balance[p1] -= amount
            balance[p2] += amount
        
        debts = [b for b in balance.values() if b != 0]
        if not debts:
            return 0

        def dfs(index):
            while index < len(debts) and debts[index] == 0:
                index += 1
            if index == len(debts):
                return 0

            min_transfers = float('inf')
            for i in range(index + 1, len(debts)):
                if debts[i] * debts[index] < 0:  
                    debts[i] += debts[index]
                    min_transfers = min(min_transfers, 1 + dfs(index + 1))
                    debts[i] -= debts[index]

            return min_transfers

        return dfs(0)    
