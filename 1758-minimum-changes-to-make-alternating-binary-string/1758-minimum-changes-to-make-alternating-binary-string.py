class Solution:
    def minOperations(self, s: str) -> int:
        zero = 0
        one = 0
        
        for i in range(0, len(s)):
            if i % 2 == 0:
                if s[i] == "1":
                    zero += 1
                else:
                    one += 1
            else:
                if s[i] == "1":
                    one += 1
                else:
                    zero += 1
        return min(zero, one)