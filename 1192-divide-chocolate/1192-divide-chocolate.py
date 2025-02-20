class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        s, e = min(sweetness), sum(sweetness) // (k + 1)

        def can_split(mid):
            count, curr = 0, 0
            for sweet in sweetness:
                curr += sweet
                if curr >= mid:
                    count += 1
                    curr = 0
            return count >= k + 1

        while s < e:
            mid = (s + e + 1) // 2
            if can_split(mid):
                s = mid
            else:
                e = mid - 1
        return s