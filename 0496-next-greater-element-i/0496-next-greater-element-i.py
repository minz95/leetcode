class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = {}

        for num in nums2:
            while stack and num > stack[-1]:
                hmap[stack.pop()] = num
            stack.append(num)

        while stack:
            hmap[stack.pop()] = -1

        return [hmap.get(i, -1) for i in nums1]    
