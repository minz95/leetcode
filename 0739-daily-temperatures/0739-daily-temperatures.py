class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[stack[-1]] < t:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer