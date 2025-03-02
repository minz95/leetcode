class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            k1, v1 = nums1[i]
            k2, v2 = nums2[j]
            if k1 < k2:
                result.append([k1, v1])
                i += 1
            elif k1 == k2:
                result.append([k1, v1 + v2])
                i += 1
                j += 1
            else:
                result.append([k2, v2])
                j += 1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        return result