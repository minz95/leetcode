from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        product = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                curr = nums[i] * nums[j]
                product[curr] += 1
                
        for p in product.values():
            if p > 1:
                count += (p * (p - 1) // 2) * 8
            
        return count
            