class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)

        for c in s:
            stack.append(c)
            if len(stack) >= n and "".join(stack[-n:]) == part:
                for _ in range(n):
                    stack.pop()
            
        return "".join(stack)