class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ready = {}

        for n in nums:
            s = sum([int(i) for i in str(n)])
            if s not in ready:
                ready[s] = [n]
            else:
                ready[s].append(n)
        max_sum = -1
        for k, v in ready.items():
            if len(v) > 1:
                v.sort()
                max_sum = max(max_sum, v[-1] + v[-2])
        return max_sum