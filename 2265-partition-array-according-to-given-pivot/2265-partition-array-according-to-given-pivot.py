class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        prev = []
        same = []
        post = []
        for n in nums:
            if n < pivot:
                prev.append(n)
            elif n == pivot:
                same.append(n)
            else:
                post.append(n)
        return prev + same + post