class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            found = False
            for idx, j in enumerate(nums2):
                if found and j > i:
                    result.append(j)
                    break
                if j == i:
                    found = True
                if idx == len(nums2) - 1:
                    result.append(-1)
        return result
