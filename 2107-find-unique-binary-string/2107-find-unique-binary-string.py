class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def backtrack(idx, curr):
            if idx == len(nums[0]):
                if "".join(curr) not in nums:
                    return curr
                else:
                    return []
            for c in "01":
                curr.append(c)
                result = backtrack(idx+1, curr)
                if result:
                    return result
                curr.pop()
            return []
        
        return "".join(backtrack(0, []))
            