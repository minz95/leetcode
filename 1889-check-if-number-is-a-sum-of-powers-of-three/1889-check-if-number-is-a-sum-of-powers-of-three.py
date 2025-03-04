class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def helper(power, k):
            if k == 0:
                return True
            if 3**power > k:
                return False
            add = helper(power+1, k-3**power)
            skip = helper(power+1, k)
            return add or skip
        return helper(0, n)