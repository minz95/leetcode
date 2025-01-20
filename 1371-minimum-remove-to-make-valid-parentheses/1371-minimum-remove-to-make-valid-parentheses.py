class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removes = []
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) == 0:
                    removes.append(i)
                else:
                    stack.pop()

        result = ""
        for i, c in enumerate(s):
            if i not in removes and i not in stack:
                result += c
        return result