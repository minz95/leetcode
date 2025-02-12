class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)

        if total % k != 0:
            return False
        
        target = total // k
        taken = ['0'] * n
        memo = {}
        nums.sort(reverse=True)

        def backtrack(index: int, count: int, curr: int) -> bool:
            n = len(nums)
            s = ''.join(taken)

            if count == k-1:
                return True
            if curr > target:
                return False
            if s in memo:
                return memo[s]
            if curr == target:
                memo[s] = backtrack(0, count + 1, 0)
                return memo[s]
            for j in range(n):
                if taken[j] == '0':
                    taken[j] = '1'
                    if backtrack(j+1, count, curr+nums[j]):
                        return True
                    taken[j] = '0'
            memo[s] = False
            return memo[s]
        return backtrack(0, 0, 0)