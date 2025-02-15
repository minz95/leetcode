class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(s, target, idx=0, curr=0):
            if idx == len(s):
                return curr == target
            for i in range(idx, len(s)):
                num = int(s[idx:i+1])
                if backtrack(s, target, i+1, curr+num):
                    return True
            return False
        
        result = 0
        for i in range(1, n + 1):
            si = str(i * i)
            if backtrack(si, i):
                result += i * i
        return result