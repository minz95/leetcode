class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total = 0
        k = 0
        diff = [0] * (n + 1)

        for i in range(n):
            while total + diff[i] < nums[i]:
                k += 1

                if k > len(queries):
                    return -1
                left, right, val = queries[k-1]

                if right >= i:
                    diff[max(left, i)] += val
                    diff[right + 1] -= val
            total += diff[i]
        return k
