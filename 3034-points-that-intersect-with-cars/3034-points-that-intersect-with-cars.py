from collections import defaultdict
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key = lambda x: x[0])
        line = defaultdict(int)

        mins = nums[0][0]
        maxe = nums[0][1]
        for i, n in enumerate(nums):
            s, e = n[0], n[1]
            line[s] += 1
            line[e+1] -= 1
            if maxe < e:
                maxe = e
        cover = 0
        count = 0
        for i in range(mins, maxe+2):
            count += line[i]
            if count > 0:
                cover += 1
        return cover